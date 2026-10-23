#!/usr/bin/env python3
"""Verschlüsselung für Lukas' Ja/Nein-Antworten und Notizen im öffentlichen Repo.

Schlüssel: GitHub-Secret DATEN_SCHLUESSEL (beliebiges langes Passwort) -> SHA-256 -> AES-256-GCM.
Ohne Secret bleibt alles wie bisher im Klartext. Alte Klartext-Dateien werden weiter gelesen.

  seal(obj)   -> {"_enc": "v1", "n": ..., "c": ...}   (ohne Schlüssel: obj unverändert)
  unwrap(doc) -> entschlüsselt ganze Dateien und das Feld „lukas_enc“ der Live-Dateien
"""

import base64
import hashlib
import json
import os

ENV = "DATEN_SCHLUESSEL"


def _key():
    secret = os.environ.get(ENV, "")
    return hashlib.sha256(("trader-vault:" + secret).encode("utf-8")).digest() if secret else None


def enabled():
    return _key() is not None


def seal(obj):
    key = _key()
    if not key:
        return obj
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    nonce = os.urandom(12)
    ct = AESGCM(key).encrypt(nonce, json.dumps(obj, ensure_ascii=False).encode("utf-8"), b"trader")
    return {"_enc": "v1", "n": base64.b64encode(nonce).decode(), "c": base64.b64encode(ct).decode()}


def _open(box, default):
    key = _key()
    if not key:
        return default                       # verschlüsselt, aber kein Schlüssel da: wie leer behandeln
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    try:
        raw = AESGCM(key).decrypt(base64.b64decode(box["n"]), base64.b64decode(box["c"]), b"trader")
    except Exception:
        return default                       # falscher Schlüssel
    return json.loads(raw.decode("utf-8"))


def unwrap(doc):
    if isinstance(doc, dict) and doc.get("_enc") == "v1":
        return _open(doc, {})
    if isinstance(doc, dict) and isinstance(doc.get("lukas_enc"), dict):
        doc = dict(doc)
        doc["lukas"] = _open(doc.pop("lukas_enc"), [])
    return doc


def selftest():
    os.environ[ENV] = "test-passwort"
    box = seal({"20261023-AAPL-orb": {"answer": "ja", "ts": 1}})
    assert box["_enc"] == "v1" and "AAPL" not in json.dumps(box)
    assert unwrap(box) == {"20261023-AAPL-orb": {"answer": "ja", "ts": 1}}
    doc = unwrap({"date": "x", "lukas": [], "lukas_enc": seal([{"symbol": "AAPL"}])})
    assert doc["lukas"] == [{"symbol": "AAPL"}] and "lukas_enc" not in doc
    assert unwrap({"a": 1}) == {"a": 1}
    os.environ[ENV] = "falsch"
    assert unwrap(box) == {}
    del os.environ[ENV]
    assert seal({"a": 1}) == {"a": 1} and unwrap(box) == {}
    print("Selbsttest ok: Verschlüsselung der Antworten und Notizen.")


if __name__ == "__main__":
    selftest()
