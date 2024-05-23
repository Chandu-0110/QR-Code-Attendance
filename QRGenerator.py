import qrcode

# Read the whitelist file and strip newlines
with open('../whitelist.txt', 'r') as f:
    authorized = [line.strip() for line in f if len(line.strip()) > 2]

# Generate and save a QR code for each authorized entry
for entry in authorized:
    qr = qrcode.make(entry)
    qr.save(f"{entry}.png")

