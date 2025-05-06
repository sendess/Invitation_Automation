import qrcode
from PIL import Image

# The text you want to encode in the QR code
data = "Mr. Naresh Khapangi"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=0,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Resize the image to 980x980 pixels
resized_img = img.resize((245, 245))

# Save the resized image as a PNG file
resized_img.save("qr_code.png")

print("QR code saved as my_qrcode.png with resolution 980x980.")