from PIL import Image, ImageFilter

img = Image.open("./Astro/astro.jpg")

# to preserve the original aspect ratio
# given ratio is the range within which
# we want our image to be
img.thumbnail((400, 400))
img.save("thumbnail.jpg")

print(img.size)
