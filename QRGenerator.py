import qrcode

with open('../whitelist.txt', 'r') as f:
    authorized = [l[:-1] for l in f.readlines() if len(l)>2]

for i in range(len(authorized)):
    qr = qrcode.make(authorized[i])
    qr.save(authorized[i])