from PIL import Image
import os
from bbs.settings import MEDIA_ROOT


def image_change(filename, width=200, height=200):
    image = Image.open(filename)
    new_image = image.resize((width, height), Image.ANTIALIAS)
    new_image.save('new_'+filename)
    new_image.close()


files = os.listdir('.')
for file in files:
    if file.split('.')[-1] == 'png':
        image_change(file, 30, 30)