import pybase64
import binascii

def decode_base64(encoded):
    """
    Decodes a base64 encoded string using multiple encodings for compatibility.
    """
    decoded = ""
    for encoding in ["utf-8", "iso-8859-1"]:
        try:
            # Add padding if necessary
            decoded = pybase64.b64decode(encoded + b"=" * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded