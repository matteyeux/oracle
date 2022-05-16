from secrets import token_bytes

from oracle.anya.anya import *
from oracle.anya.exceptions import *

from typing import Optional


def decrypt(kbag: str = None, do_sep: bool = False, ecid: int = None) -> Optional[str]:
    """Decrypt AP or SEP kbag."""
    if kbag is None or len(kbag) != 96:
        return None

    dev = AnyaDevice(ecid=ecid)

    try:
        dev.connect()
    except AnyaError as e:
        print(f"failed to connect: {str(e)}")
        return None

    if do_sep is True:
        try:
            if not dev.ping_sep():
                print("SEP is unreachable")
                dev.disconnect()
                return None
        except AnyaUSBError as e:
            print(f"failed to ping SEP: {str(e)}")
            dev.disconnect()
            return None

    try:
        decoded = decode_kbag(kbag)
    except AnyaValueError as e:
        print(f"failed to parse KBAG: {str(e)}")
        dev.disconnect()
        return None

    try:
        key = dev.decrypt_kbag(decoded, sep=do_sep)
    except AnyaUSBError as e:
        print(f"failed to decrypt KBAG: {str(e)}")
        dev.disconnect()
        return None

    print(encode_key(key, True))
    return encode_key(key, True)
