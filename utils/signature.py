from secp256k1 import PublicKey, ALL_FLAGS

from base58 import b58encode, b58decode
from utils.hash import ripemd160, sha256


def recover_user_id(msg, signature):
    if isinstance(msg, str):
        msg = msg.encode('utf8')

    key = PublicKey(flags=ALL_FLAGS)
    sig = b58decode(signature)
    sig = key.ecdsa_recoverable_deserialize(sig[1:], sig[0] - 31)
    key.public_key = key.ecdsa_recover(msg, sig)
    serialized_pubkey = key.serialize(True)
    hashed = b'\x00' + ripemd160(sha256(serialized_pubkey))
    checksum = sha256(sha256(hashed))[:4]
    return b58encode(hashed + checksum).decode('ascii')
