from PIL import Image, ImageDraw, ImageFont

def create_image(text):
    text = text.lower()
    path = "bg.jpg"
    im = Image.open(path)
    font = ImageFont.truetype("./Fonts/font2.ttf", 30)
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(text, font)
    W, H = im.size
    coord = ((W-w)/2, (H-h)/2)
    draw.text(coord, text, fill="white", font=font)
    im.save(f"./Images/{text}.jpg")
    return f"./Images/{text}.jpg"
