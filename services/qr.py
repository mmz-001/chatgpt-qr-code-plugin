import qrcode
from io import BytesIO


def generate_qr_code_from_string(string: str) -> BytesIO:
    """Generate a QR code from a string and return a BytesIO object"""
    img = qrcode.make(string)
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")

    return img_buffer
