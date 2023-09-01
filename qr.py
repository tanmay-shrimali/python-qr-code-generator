import qrcode

content = "xxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with the content you want to encode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(content)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("D:\qr_code.png")  # Save the QR code as an image file in location
