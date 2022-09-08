from PIL import Image, ImageDraw, ImageFilter
import os

def generateImage(qrcodeImagePath,id):
    templateImage = Image.open('image-template.png')
    qrCodeImage = Image.open(qrcodeImagePath)

    resizedImage = qrCodeImage.resize(size=[550,613])

    backImage = templateImage.copy()
    backImage.paste(resizedImage,(190,720))
    imagename = 'output/image_{}.png'.format(id)
    
    backImage.save(imagename,quality=100)
    print('---saved---',imagename)



INPUTDIR = 'qrcodes_images'

if(not os.path.exists('output')):
    os.mkdir('output')
qrcodeimages = os.listdir(INPUTDIR)

for i,qrcode_image in enumerate(qrcodeimages):
    imagepath = os.path.join(INPUTDIR,qrcode_image)
    generateImage(qrcodeImagePath=imagepath,id=str(i))