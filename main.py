import base64
import json
import qrcode
import qrcode.image.svg
from PIL import Image, ImageFont, ImageDraw
import tkinter as tk
from tkinter import Tk, font, ttk, StringVar, Frame, Canvas, PhotoImage
import os, sys


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


def app_path(path):
    frozen = "not"
    if getattr(sys, "frozen", False):
        # we are running in executable mode
        frozen = "ever so"
        app_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        app_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(app_dir, path)


def build_sign():
    # * Get input
    opn = txt_title_body.get()

    if not opn:
        lbl_status_body.configure(foreground="red")
        txt_status.set("Please enter a title")
        reset_status()
        return
    else:
        txt_status.set("")

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
    bg = Image.open(app_path("assets/background.png"))

    qr_pos = ((bg.size[0] - img.size[0]) // 2, (bg.size[1] - img.size[1]) // 2 - 126)

    bg.paste(img, qr_pos)

    # * Add text to image
    title_font = ImageFont.truetype(app_path("assets/Roboto-Bold.ttf"), 34)
    address_font = ImageFont.truetype(app_path("assets/Roboto-Regular.ttf"), 24)

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

    try:
        bg.save(f"{title}.png")
        lbl_status_body.configure(foreground="#647687")
        txt_status.set("Saved successfully")
    except:
        lbl_status_body.configure(foreground="red")
        txt_status.set("An error occured while saving")

    reset_status()


def clear_all():
    txt_title_body.set("")
    txt_address_body.set("")
    txt_suburb_body.set("")
    txt_city_body.set("")
    lbl_status_body.configure(foreground="#647687")
    txt_status.set("All cleared")
    reset_status()


def reset_status():
    root.after(2500, lambda: txt_status.set(""))


# ==================[ TKINTER SECTION ]================== #

# * Create main display
root = Tk()
root.configure(background="#647687")

# Set window icon/logo
root.iconphoto(False, tk.PhotoImage(file=app_path("assets/logo_icon.png")))

window_width = 725
window_height = 415

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


# * Load fonts
font_label = font.Font(family="Helvetica", size=12, weight="normal")
font_sub_label = font.Font(family="Helvetica", size=10, weight="normal")
font_input = font.Font(family="Helvetica", size=12, weight="normal")
font_spacer = font.Font(family="Helvetica", size=1, weight="normal")
font_button = font.Font(family="Helvetica", size=12, weight="bold")
font_status = font.Font(family="Helvetica", size=11, weight="bold")
font_info = font.Font(family="Helvetica", size=10, weight="normal")


# * Background canvas
# Create canvas
cnv_bg = Canvas(root, width=window_width, height=window_height, bg="#647687", highlightthickness=0)
# cnv_bg.grid(column=0, row=0, padx=0, pady=0, sticky="nw")
cnv_bg.pack()

# Add background image
img_app_bg = PhotoImage(file=app_path("assets/app_bg.png"))
cnv_bg.create_image(0.5, 0.5, anchor="nw", image=img_app_bg)


# * Frames
# Create
frm_inputs = Frame(bg="white", padx=20, pady=20)
frm_title = Frame(frm_inputs, bg="white", padx=0, pady=0)

# Layout
frm_title.grid(column=0, row=0, columnspan=3, sticky="ew")

# Column config
frm_inputs.columnconfigure(1, weight=1)
frm_inputs.rowconfigure(12, weight=1)
frm_title.columnconfigure(1, weight=1)


# * Add window to canvas to contain frame
win_main_frame = cnv_bg.create_window(30, 30, window=frm_inputs, anchor="nw", width=345)


# * Text input
# Title entry
lbl_title_body = ttk.Label(frm_title, text="Title", font=font_label, background="white")
lbl_title_body.grid(column=0, row=0, sticky="w", pady=0)
lbl_required = ttk.Label(frm_title, text="(required)", font=font_sub_label, background="white", foreground="red")
lbl_required.grid(column=1, row=0, sticky="w")
txt_title_body = StringVar()
ent_title_body = ttk.Entry(frm_title, textvariable=txt_title_body, font=font_input)
ent_title_body.grid(column=0, columnspan=3, row=1, pady=4, ipady=3, sticky="ew")
ent_title_body.focus()

# Spacer
lbl_spacer_body = ttk.Label(frm_inputs, text="", font=font_spacer, background="white")
lbl_spacer_body.grid(column=0, row=2, sticky="w", pady=0)

# Address entry
lbl_address_body = ttk.Label(frm_inputs, text="Address", font=font_label, background="white")
lbl_address_body.grid(column=0, row=3, sticky="w", pady=0)
txt_address_body = StringVar()
ent_address_body = ttk.Entry(frm_inputs, textvariable=txt_address_body, font=font_input)
ent_address_body.grid(column=0, columnspan=3, row=4, pady=4, ipady=3, sticky="ew")

# Spacer
lbl_spacer_body = ttk.Label(frm_inputs, text="", font=font_spacer, background="white")
lbl_spacer_body.grid(column=0, row=5, sticky="w", pady=0)

# Suburb entry
lbl_suburb_body = ttk.Label(frm_inputs, text="Suburb", font=font_label, background="white")
lbl_suburb_body.grid(column=0, row=6, sticky="w", pady=0)
txt_suburb_body = StringVar()
ent_suburb_body = ttk.Entry(frm_inputs, textvariable=txt_suburb_body, font=font_input)
ent_suburb_body.grid(column=0, columnspan=3, row=7, pady=4, ipady=3, sticky="ew")

# Spacer
lbl_spacer_body = ttk.Label(frm_inputs, text="", font=font_spacer, background="white")
lbl_spacer_body.grid(column=0, row=8, sticky="w", pady=0)

# City entry
lbl_city_body = ttk.Label(frm_inputs, text="City", font=font_label, background="white")
lbl_city_body.grid(column=0, row=9, sticky="w", pady=0)
txt_city_body = StringVar()
ent_city_body = ttk.Entry(frm_inputs, textvariable=txt_city_body, font=font_input)
ent_city_body.grid(column=0, columnspan=3, row=10, pady=4, ipady=3, sticky="ew")

# Spacer
lbl_spacer_body = ttk.Label(frm_inputs, text="", font=font_spacer, background="white")
lbl_spacer_body.grid(column=0, row=11, sticky="w", pady=4)


# * Buttons and Status
# Clear All
stl_clear = ttk.Style()
stl_clear.theme_use("alt")
stl_clear.configure("clear.TButton", background="#ff8000", foreground="white", width=5, borderwidth=0, focuscolor="none", font=font_button)
stl_clear.map("clear.TButton", background=[("active", "#ff8000")])
btn_clear = ttk.Button(frm_inputs, text="Clear All", command=clear_all, padding=7, style="clear.TButton")
btn_clear.grid(column=0, row=12)

# Status
txt_status = StringVar()
lbl_status_body = ttk.Label(
    frm_inputs,
    textvariable=txt_status,
    font=font_status,
    foreground="#647687",
    background="white",
    justify="center",
    padding=0,
)
lbl_status_body.grid(column=1, row=12, pady=5)

# Save
stl_save = ttk.Style()
stl_save.theme_use("alt")
stl_save.configure("save.TButton", background="#3399ff", foreground="white", width=5, borderwidth=0, focuscolor="none", font=font_button)
stl_save.map("save.TButton", background=[("active", "#3399ff")])
btn_save = ttk.Button(frm_inputs, text="Save", command=build_sign, padding=7, style="save.TButton")
btn_save.grid(column=2, row=12)


# * Logo
img_logo = PhotoImage(file=app_path("assets/logo.png"))
cnv_bg.create_image(550, 155, anchor="center", image=img_logo)


# * Info
text_item = cnv_bg.create_text(
    550,
    335,
    anchor="center",
    text="The image that gets created is saved\nto the same folder as this application\n\nCreated by James Rollinson, 2022",
    font=font_info,
    fill="white",
    justify="center",
)
bbox = cnv_bg.bbox(text_item)
rect_item = cnv_bg.create_rectangle(bbox, outline="#647687", fill="#647687", width=25)
cnv_bg.tag_raise(text_item, rect_item)


if __name__ == "__main__":
    # * Start main loop
    root.mainloop()
