from PIL import Image, ImageDraw, ImageFont
from . import WORDS
import random

def create_image(path, text):
    im = Image.open(path)
    font = ImageFont.truetype("./Fonts/test2.ttf")
    draw = ImageDraw.Draw(im)
    text = random.choice(WORDS)
