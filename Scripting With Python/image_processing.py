from PIL import Image, ImageFilter

image = Image.open('images\\original.jpg')
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('images\\Blurred.jpg', 'jpeg')
