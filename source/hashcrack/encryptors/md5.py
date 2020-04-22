import hashlib

def enc(h):
    return hashlib.md5(h.encode("utf-8")).hexdigest()