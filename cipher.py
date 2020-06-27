  
def load_words():
    words = open('words_alpha.txt')
    text = words.read().split()
    return text[:25]
print(load_words())