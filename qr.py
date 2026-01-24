import qrcode

qr_data = "https://https://github.com/KONIJETIYAMINI/capstone-qr/"

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("Capstone_UI_QR.png")

print("QR Code generated successfully")

