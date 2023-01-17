from PIL import Image, ImageDraw, ImageFont

def create_image(path, text):
    im = Image.open(path)
    font = ImageFont.truetype("./Fonts/test2.ttf")
    draw = ImageDraw.Draw(im)
