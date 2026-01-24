import qrcode

url = "https://konijetiyamini.github.io/QR_generator/"

qr = qrcode.make(url)
qr.save("Capstone_Project_QR.png")

print("QR Code ready")




