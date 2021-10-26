from PIL import Image

im = Image.open("lighthouse.jpg")
(width, height) = im.size
print(width)
print(height)