import qrcode
import os

if not os.path.exists('qrcodes_images'):
    os.mkdir('qrcodes_images')

for i in range(1,400):
    img = qrcode.make('Here is the QR code image no.{}'.format(str(i)))
    img.save('qrcodes_images/qrcode_test_{}.png'.format(str(i)))
