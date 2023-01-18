from PIL import Image, ImageDraw, ImageFont
from . import WORDS
import random

def create_image(path, text):
    im = Image.open(path)
    font = ImageFont.truetype("./Fonts/test2.ttf", 30)
    draw = ImageDraw.Draw(im)
    text = random.choice(WORDS)
    w, h = draw.textsize(text, font)
    W, H = im.size
    coord = ((W-w)/2, (H-h)/2)
    draw.text(coord, text, fill="white", font=font)
    im.save("splfw.png")
    return "splfw.png"
