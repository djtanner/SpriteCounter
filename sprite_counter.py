import sys
from PIL import Image, ImageDraw

if len(sys.argv) != 4:
    while True:
        print("Please enter the name of the file followed by the width of the sprite and the height of the sprite.")
        user_input = input("Enter the arguments: ")
        args = user_input.split()
        if len(args) == 3:
            break
    sys.argv[1:] = args


imageLocation = sys.argv[1]
sprite_width = int(sys.argv[2])
sprite_height = int(sys.argv[3])


image = Image.open(imageLocation)
image = image.convert("RGB")

draw = ImageDraw.Draw(image)

width = image.width
height = image.height

counter = 1


for y in range(0, int(height/sprite_height)):
    for x in range(0, int(width/sprite_width)):
        draw.text((x*sprite_width, y*sprite_height),
                  str(counter), fill="white")
        counter += 1


image.save("output.jpg")
