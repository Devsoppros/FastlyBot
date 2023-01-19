from hlpl_english_words import english_words
import requests
from config import BACKGROUND_URL as image_url

case=['adjective','adverb','noun-singular','noun-plural','verb','article']

WORDS = []

def load_words():
    global WORDS 
    for mad in case:
        for red in english_words.get(mad):
            if len(red) >= 7:
                WORDS.append(red)

def load_bg():
    img_data = requests.get(image_url).content
    with open('bg.jpg', 'wb') as handler:
        handler.write(img_data)
