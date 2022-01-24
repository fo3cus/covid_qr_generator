import base64
import json
import tkinter
import qrcode
import qrcode.image.svg
from PIL import Image, ImageFont, ImageDraw
from tkinter import Tk, font, ttk, StringVar, Entry
from tkinter.filedialog import asksaveasfile

# * Static data
SAMPLE_DICT = {
    "typ": "entry",
    "gln": "0000000000000",
    "opn": "COVID Test Location",
    "adr": "123 Test Street\nTest Suburb\nCity",
    "ver": "c19:1",
}
COV_PREFIX = "NZCOVIDTRACER:"


# ==================[ FUNCTIONS SECTION ]================== #


def build_sign():
    # * Get input
    # Sample input data
    opn = "Custom Test Locale"
    adr = "123 Test Street\nTest Suburb\nCity"

    # * Construct dictionary from input
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
    bg = Image.open("assets/background.png")

    qr_pos = ((bg.size[0] - img.size[0]) // 2, (bg.size[1] - img.size[1]) // 2 - 126)

    bg.paste(img, qr_pos)

    # * Add text to image
    title_font = ImageFont.truetype("assets/Roboto-Bold.ttf", 34)
    address_font = ImageFont.truetype("assets/Roboto-Regular.ttf", 24)

    title_text = opn.strip()
    address_text = adr.replace("\n", ", ")

    print(title_text)
    print(address_text)

    image_editable = ImageDraw.Draw(bg)

    title_w, _ = image_editable.textsize(title_text, font=title_font)
    title_x = (bg.size[0] - title_w) // 2
    title_y = 658
    image_editable.text((title_x, title_y), title_text, (0, 0, 0), font=title_font)

    address_w, _ = image_editable.textsize(address_text, font=address_font)
    address_x = (bg.size[0] - address_w) // 2
    address_y = 698
    image_editable.text((address_x, address_y), address_text, (0, 0, 0), font=address_font)

    # * Save final image
    title = opn.replace(" ", "_").lower()

    bg.save(f"{title}.png")


# * Close all windows
def quit_all(*args):
    root.destroy()


# ==================[ TKINTER SECTION ]================== #

# * Create main display
root = Tk()
root.configure(background="white")

window_width = 500
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.resizable(False, False)
root.title("NZ COVID QR Sign Generator")


# * Set up form display
font_title = font.Font(family="Helvetica", size=20, weight="bold")
font_input = font.Font(family="Helvetica", size=18, weight="normal")
font_label = font.Font(family="Helvetica", size=16, weight="normal")

txt_title = StringVar()
txtbox_title = Entry(root, textvariable=txt_title)

txt_address = StringVar()
txtbox_address = Entry(root, textvariable=txt_address)

txt_suburb = StringVar()
txtbox_suburb = Entry(root, textvariable=txt_suburb)

txt_city = StringVar()
txtbox_city = Entry(root, textvariable=txt_city)

# * Text input
# Banner
lbl_banner = ttk.Label(root, text="Enter Title and Address", font=font_title, foreground="black", background="white")
lbl_banner.grid(column=0, row=0, columnspan=2, padx=5, pady=10)

# Title entry
lbl_title = ttk.Label(root, text="Title", font=font_label, foreground="black", background="white")
lbl_title.grid(column=0, row=1, padx=5, pady=10, sticky=tkinter.E)

ent_title = ttk.Entry(root, textvariable=txt_title, font=font_input, width=25)
ent_title.grid(column=1, row=1, padx=5, pady=10, ipady=5)
ent_title.focus()

# Address entry
lbl_address = ttk.Label(root, text="Address", font=font_label, foreground="black", background="white")
lbl_address.grid(column=0, row=2, padx=5, pady=10)

ent_address = ttk.Entry(root, textvariable=txt_address, font=font_input, width=25)
ent_address.grid(column=1, row=2, padx=5, pady=10, ipady=5)
ent_address.focus()

# Suburb entry
lbl_suburb = ttk.Label(root, text="Suburb", font=font_label, foreground="black", background="white")
lbl_suburb.grid(column=0, row=3, padx=5, pady=10, ipady=5)

ent_suburb = ttk.Entry(root, textvariable=txt_suburb, font=font_input, width=25)
ent_suburb.grid(column=1, row=3, padx=5, pady=10, ipady=5)
ent_suburb.focus()

# City entry
lbl_city = ttk.Label(root, text="City", font=font_label, foreground="black", background="white")
lbl_city.grid(column=0, row=4, padx=5, pady=10)

ent_city = ttk.Entry(root, textvariable=txt_city, font=font_input, width=25)
ent_city.grid(column=1, row=4, padx=5, pady=10, ipady=5)
ent_city.focus()


# * Save button
btn_save = ttk.Button(root, text="Save", command=build_sign)
btn_save.grid(column=0, row=5, columnspan=2, padx=5, pady=10)


if __name__ == "__main__":
    # * Start main loop
    root.mainloop()
