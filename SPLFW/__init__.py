from hlpl_english_words import english_words

case=['adjective','adverb','noun-singular','noun-plural','verb','article']

WORDS = []

def load_words():
    global WORDS 
    for mad in case:
        for red in english_words.get(mad):
            if len(red) >= 7:
                WORDS.append(red)
