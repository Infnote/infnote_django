import hashlib


def sha256(data: bytes) -> bytes:
    if isinstance(data, bytes):
        return hashlib.sha256(data).digest()
    else:
        raise TypeError('Data must be "bytes".')


def ripemd160(data: bytes) -> bytes:
    if isinstance(data, bytes):
        h = hashlib.new('ripemd160')
        h.update(data)
        return h.digest()
    else:
        raise TypeError('Data must be "bytes".')
