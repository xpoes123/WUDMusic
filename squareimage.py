from PIL import Image
import os

image = Image.open('insta2.webp')
new_image = image.resize((500,500))
new_image.save('insta2.webp')

# directory = 'home/static/home/images/november'
# for i in os.listdir(directory):
#     # print(i)
#     image = Image.open(f'{directory}/{i}')
#     new_image = image.resize((500,500))
#     new_image.save(f'{directory}/resized/{i}')