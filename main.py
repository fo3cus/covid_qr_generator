import base64
import json
import qrcode
import qrcode.image.svg
from PIL import Image, ImageFont, ImageDraw
import tkinter as tk
from tkinter import Tk, font, ttk, StringVar, Frame


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
    opn = txt_title_body.get()

    if not opn:
        lbl_warning_text.set("YOU MUST ENTER A TITLE")
        return
    else:
        lbl_warning_text.set("")

    entries = [txt_address_body.get(), txt_suburb_body.get(), txt_city_body.get()]

    adr = ""

    prev = False  # Flag to check for previous entry, thus needs \n

    for index, entry in enumerate(entries):
        if entry:
            if index == 0:
                adr += entry
                prev = True
            else:
                if prev:  # Previous entry exists
                    adr += "\n" + entry
                else:
                    adr += entry
                    prev = True

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


# ==================[ TKINTER SECTION ]================== #

# * Create main display
root = Tk()
root.configure(background="#F4F4F4")

# Set window icon/logo
root.iconphoto(False, tk.PhotoImage(file="assets/logo.png"))

window_width = 500
window_height = 705

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.resizable(False, False)
root.title("NZ COVID QR Sign Generator")
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)


# * Set up form display
font_title = font.Font(family="Helvetica", size=20, weight="bold")
font_request = font.Font(family="Helvetica", size=16, weight="bold")
font_input = font.Font(family="Helvetica", size=18, weight="normal")
font_label = font.Font(family="Helvetica", size=16, weight="bold")
font_sub_label = font.Font(family="Helvetica", size=10, weight="normal")


# * Frames
# Create
frm_banner = Frame(root, bg="#FFCC00")
frm_request = Frame(root, bg="#F4F4F4")
frm_title_outer = Frame(root, bg="#F4F4F4", padx=15, pady=10)
frm_title_inner = Frame(frm_title_outer, bg="white")
frm_title_stripe = Frame(frm_title_inner, bg="#FFCC00", padx=5)
frm_title_body = Frame(frm_title_inner, bg="white", padx=15, pady=15)
frm_address_outer = Frame(root, bg="#F4F4F4", padx=15, pady=10)
frm_address_inner = Frame(frm_address_outer, bg="white")
frm_address_stripe = Frame(frm_address_inner, bg="#FFCC00", padx=5)
frm_address_body = Frame(frm_address_inner, bg="white", padx=15, pady=15)
frm_suburb_outer = Frame(root, bg="#F4F4F4", padx=15, pady=10)
frm_suburb_inner = Frame(frm_suburb_outer, bg="white")
frm_suburb_stripe = Frame(frm_suburb_inner, bg="#FFCC00", padx=5)
frm_suburb_body = Frame(frm_suburb_inner, bg="white", padx=15, pady=15)
frm_city_outer = Frame(root, bg="#F4F4F4", padx=15, pady=10)
frm_city_inner = Frame(frm_city_outer, bg="white")
frm_city_stripe = Frame(frm_city_inner, bg="#FFCC00", padx=5)
frm_city_body = Frame(frm_city_inner, bg="white", padx=15, pady=15)
frm_save = Frame(root, bg="#F4F4F4", padx=15, pady=5)

# Layout
frm_banner.grid(column=0, sticky="we")
frm_request.grid(column=0, sticky="we")
frm_title_outer.grid(column=0, sticky="we")
frm_title_inner.grid(column=0, sticky="we")
frm_title_stripe.grid(column=0, row=0, sticky="nesw")
frm_title_body.grid(column=1, row=0, sticky="nesw")
frm_address_outer.grid(column=0, sticky="we")
frm_address_inner.grid(column=0, sticky="we")
frm_address_stripe.grid(column=0, sticky="nesw")
frm_address_body.grid(column=1, row=0, sticky="nesw")
frm_suburb_outer.grid(column=0, sticky="we")
frm_suburb_inner.grid(column=0, sticky="we")
frm_suburb_stripe.grid(column=0, sticky="nesw")
frm_suburb_body.grid(column=1, row=0, sticky="nesw")
frm_city_outer.grid(column=0, sticky="we")
frm_city_inner.grid(column=0, sticky="we")
frm_city_stripe.grid(column=0, sticky="nesw")
frm_city_body.grid(column=1, row=0, sticky="nesw")
frm_save.grid(column=0, sticky="we")

# Column config
frm_banner.columnconfigure(0, weight=1)
frm_request.columnconfigure(0, weight=1)
frm_title_outer.columnconfigure(0, weight=1)
frm_title_inner.columnconfigure(1, weight=1)
frm_title_body.columnconfigure(2, weight=1)
frm_address_outer.columnconfigure(0, weight=1)
frm_address_inner.columnconfigure(1, weight=1)
frm_address_body.columnconfigure(1, weight=1)
frm_suburb_outer.columnconfigure(0, weight=1)
frm_suburb_inner.columnconfigure(1, weight=1)
frm_suburb_body.columnconfigure(1, weight=1)
frm_city_outer.columnconfigure(0, weight=1)
frm_city_inner.columnconfigure(1, weight=1)
frm_city_body.columnconfigure(1, weight=1)
frm_save.columnconfigure(0, weight=1)

# * Text input
# Banner
lbl_banner = ttk.Label(frm_banner, text="NZ COVID QR Sign Generator", font=font_title, background="#FFCC00")
lbl_banner.grid(column=0, pady=20)

# Request
lbl_request = ttk.Label(frm_request, text="Please enter a title and address", font=font_request, foreground="#545454", background="#F4F4F4")
lbl_request.grid(column=0, row=0, padx=0, pady=20)

# Title entry
lbl_title_stripe = ttk.Label(frm_title_stripe, text="", font=font_label, background="#FFCC00")
lbl_title_stripe.grid(column=0, row=0, sticky="w")
lbl_title_body = ttk.Label(frm_title_body, text="Title", font=font_label, background="white")
lbl_title_body.grid(column=0, row=0, sticky="w")
lbl_required = ttk.Label(frm_title_body, text="(required)", font=font_sub_label, background="white", foreground="red")
lbl_required.grid(column=1, row=0, sticky="w")
lbl_warning_text = StringVar()
lbl_warning = ttk.Label(frm_title_body, text="", font=font_sub_label, background="white", foreground="red", textvariable=lbl_warning_text)
lbl_warning.grid(column=2, row=0)
txt_title_body = StringVar()
ent_title_body = ttk.Entry(frm_title_body, textvariable=txt_title_body, font=font_input, width=30)
ent_title_body.grid(column=0, columnspan=3, row=1, ipady=5, sticky="w")
ent_title_body.focus()

# Address entry
lbl_address_stripe = ttk.Label(frm_address_stripe, text="", font=font_label, background="#FFCC00")
lbl_address_stripe.grid(column=0, row=0, sticky="w")
lbl_address_body = ttk.Label(frm_address_body, text="Address", font=font_label, background="white")
lbl_address_body.grid(column=0, row=0, sticky="w")
txt_address_body = StringVar()
ent_address_body = ttk.Entry(frm_address_body, textvariable=txt_address_body, font=font_input, width=30)
ent_address_body.grid(column=0, row=1, ipady=5, sticky="w")

# Suburb entry
lbl_suburb_stripe = ttk.Label(frm_suburb_stripe, text="", font=font_label, background="#FFCC00")
lbl_suburb_stripe.grid(column=0, row=0, sticky="w")
lbl_suburb_body = ttk.Label(frm_suburb_body, text="Suburb", font=font_label, background="white")
lbl_suburb_body.grid(column=0, row=0, sticky="w")
txt_suburb_body = StringVar()
ent_suburb_body = ttk.Entry(frm_suburb_body, textvariable=txt_suburb_body, font=font_input, width=30)
ent_suburb_body.grid(column=0, row=1, ipady=5, sticky="w")

# City entry
lbl_city_stripe = ttk.Label(frm_city_stripe, text="", font=font_label, background="#FFCC00")
lbl_city_stripe.grid(column=0, row=0, sticky="w")
lbl_city_body = ttk.Label(frm_city_body, text="City", font=font_label, background="white")
lbl_city_body.grid(column=0, row=0, sticky="w")
txt_city_body = StringVar()
ent_city_body = ttk.Entry(frm_city_body, textvariable=txt_city_body, font=font_input, width=30)
ent_city_body.grid(column=0, row=1, ipady=5, sticky="w")


# * Save button
stl_save = ttk.Style()
stl_save.theme_use("alt")
stl_save.configure("TButton", background="black", foreground="white", width=200, borderwidth=0, focuscolor="none", font=font_request)
stl_save.map("TButton", background=[("active", "black")])
btn_save = ttk.Button(frm_save, text="Save", command=build_sign, padding=15)
btn_save.grid(column=0, columnspan=2, row=5)


if __name__ == "__main__":
    # * Start main loop
    root.mainloop()
