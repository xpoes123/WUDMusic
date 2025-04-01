from PIL import Image
import os

image = Image.open('1.png')
new_image = image.resize((500,500))
new_image.save('1.png')