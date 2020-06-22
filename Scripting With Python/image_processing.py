from PIL import Image, ImageFilter

image = Image.open('images\\original.jpg')
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('images\\Blurred.jpg', 'jpeg')

grey_image = image.convert('L')
grey_image.save('images\\Grey.png', 'png')

rotated_image = image.rotate(90)
rotated_image.save('images\\Rotated.png', 'png')

resized_image = image.resize((300, 300))
resized_image.save('images\\Resized.png', 'png')

box = (2433, 2061, 3449, 3061)
cropped_image = image.crop(box)
cropped_image.save('images\\Cropped.png', 'png')
cropped_image.show()
