'''
import qrcode
import json

# Create a QR code object
qr = qrcode.QRCode(
    version=3,  # Adjust the version as needed for larger data
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for better readability
    box_size=10,  # Adjust the size of each pixel in the QR code
    border=4  # Adjust the border width around the QR code
)
data=input("enter data for qr")
# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("my_qr_code.png")
'''

import qrcode
import json

# Collect 5 inputs from the user
data = {}
data['node'] = input("name of node: ")

# Convert the collected data to a JSON string
json_data = json.dumps(data)

# Create a QR code with the JSON data
qr = qrcode.QRCode(
    version=3,  # Adjust the version as needed for larger data
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for better readability
    box_size=10,  # Adjust the size of each pixel in the QR code
    border=4  # Adjust the border width around the QR code
)

# Add the JSON data to the QR code
qr.add_data(json_data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("my_qr_code.png")

print("QR code generated and saved as 'my_qr_code.png'.")
