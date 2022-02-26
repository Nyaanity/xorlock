from itertools import cycle
from typing import *


def xorEncrypt(
    text: str,
    key: str,
    *,
    to_hex: Optional[bool] = False,
    to_bytes: Optional[bool] = False
) -> str:
    """Encrypts a string using XOR encryption.

    Parameters
    ----------
    text : :class:`str`
        The text to encrypt.
    key : :class:`str`
        The key to use for encryption.
    to_hex : :class:`Optional[bool]`
        Whether or not the encrypted text should be converted to hex, by default False
    to_bytes : :class:`Optional[bool]`
        Whether or not the encrypted text should be converted to bytes, by default False

    Returns
    -------
    :class:`str`
        The encrypted text.
    """
    if to_hex:
        return (
            "0x"
            + "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(text, cycle(key)))
            .encode()
            .hex()
            .upper()
        )
    elif to_bytes:
        text = text.encode()
        key = key.encode()
        return bytes([x ^ y for (x, y) in zip(text, cycle(key))])
    return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(text, cycle(key)))


def xorDecrypt(
    text: str,
    key: str,
    *,
    from_hex: Optional[bool] = False,
    from_bytes: Optional[bool] = False
) -> str:
    """Decrypts a string using XOR encryption.

    Parameters
    ----------
    text : :class:`str`
        The text to decrypt.
    key : :class:`str`
        The key to use for decryption.
    to_hex : :class:`Optional[bool]`
        Whether or not the decrypted text should be converted to hex, by default False

    Returns
    -------
    :class:`str`
        The decrypted text.
    """
    if from_hex:
        if "0x" in text:
            text = text[2:]
        text = bytes.fromhex(text).decode()
        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(text, cycle(key)))
    elif from_bytes:
        key = key.encode()
        return bytes([x ^ y for (x, y) in zip(text, cycle(key))]).decode()
    return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(text, cycle(key)))
