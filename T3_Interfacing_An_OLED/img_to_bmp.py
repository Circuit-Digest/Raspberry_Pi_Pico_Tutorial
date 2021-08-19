import base64


import io
from PIL import Image

input_filename_with_path = "rpilogo1"

file_in = input_filename_with_path + ".png"
file_out = input_filename_with_path+".bmp"
img = Image.open(file_in)

img = img.transpose(Image.FLIP_LEFT_RIGHT)

threshold = 65
func = lambda x : 255 if x > threshold else 0
img = img.convert('L').point(func,mode='1')
img.save(file_out)

img = Image.open(file_out,mode='r')
img_bytes = io.BytesIO()
img.save(img_bytes,format='BMP')
img_bytes = img_bytes.getvalue()

print("Copy this bitmap array:")
print('\n')
print(img_bytes)
print('\n')
print('Image Resolution: ({0},{1})'.format(img.width,img.height))