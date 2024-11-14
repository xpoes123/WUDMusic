from PIL import Image
import os

image = Image.open('1.jpg')
new_image = image.resize((500,500))
new_image.save('1.jpg')

# directory = 'home/static/home/images/november'
# for i in os.listdir(directory):
#     # print(i)
#     image = Image.open(f'{directory}/{i}')
#     new_image = image.resize((500,500))
#     new_image.save(f'{directory}/resized/{i}')