import base64
import json
import qrcode
import qrcode.image.svg
from PIL import Image, ImageFont, ImageDraw
from qrcode.image.pure import PymagingImage


# * Data
SAMPLE_DICT = {
    "typ": "entry",
    "gln": "0000000000000",
    "opn": "COVID Test Location",
    "adr": "123 Test Street\nTest Suburb\nCity",
    "ver": "c19:1",
}
COV_PREFIX = "NZCOVIDTRACER:"


# * Accept input
# Test data
opn = "Custom Test Locale"
adr = "456 Custom Road\nSome Suburb\nCity"


# * Construct Dictionary
custom_dict = {
    "typ": "entry",
    "gln": "",
    "opn": opn,
    "adr": adr,
    "ver": "c19:1",
}


# * Convert to JSON
json_data = json.dumps(custom_dict, separators=(",", ":"))  # Converts the dictionary to a JSON object while removing extra spaces
print(json_data)


# * Encode as base64 string
json_b64 = base64.b64encode(json_data.encode("utf-8"))
print(json_b64)
base64_message = json_b64.decode("utf-8")
print(base64_message)


# * Add prefix
final_message = COV_PREFIX + base64_message


# * Convert to QR code image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(final_message)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


# * Resize img, load bg, calc position, merge
img = img.resize((450, 450))
bg = Image.open("background.png")

qr_pos = ((bg.size[0] - img.size[0]) // 2, (bg.size[1] - img.size[1]) // 2 - 126)

bg.paste(img, qr_pos)


# * Save final image
title = opn.replace(" ", "_").lower()

bg.save(f"{title}.png")
