from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

# to blur the image
filtered_img = img.filter(ImageFilter.BLUR)

# to sharpen the image
filtered_img = img.filter(ImageFilter.SHARPEN)

# convert image to greyscale
# a new copy will be created
filtered_img = img.convert("L")
filtered_img.save("./Output/grey.png", "png")

# to show the image
filtered_img.show()

# to rotate the image
rotate_img = filtered_img.rotate(90)
rotate_img.show()

# to resize the image
resize_img = filtered_img.resize((300, 300))
resize_img.save("./Output/grey.png", "png")
resize_img.show()

# to crop the image
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("./Output/grey.png", "png")
region.show()
