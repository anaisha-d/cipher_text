  
from urllib.request import urlopen

alphabet = 'abcdefghijklmnopqrstuvwxyz '
new_message = ''
key = ''
message = ''

def load_words():
    all_words = urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')
    global valid_words
    valid_words = set(all_words.read().decode().split())
    return valid_words

def ask_user():
    global key 
    key = input('Please enter a key: ')
    global message 
    message = input('Please enter a message to encrypt/decrypt: ')

  

def check_cipher():
    split_message = message.split()
    encrypt = None
    for w in split_message:
        if w.lower() in valid_words:
            encrypt = True
        else:
            encrypt = False
            break
    return encrypt
def ciphering():
    encryption = check_cipher()
    new_message = ''
    if encryption == True:
        for w in message.lower():
            if (w not in key) or (w not in alphabet):
                new_message += w
            else:
                w_index = alphabet.index(w)
                new_message += key[w_index]
    else:
        for w in message.lower():
            if (w not in key) or (w not in alphabet):
                new_message += w
            else:
                w_index = key.index(w)
                new_message += alphabet[w_index]
    return new_message


    




if __name__ == '__main__':
    english_words = load_words()
    # demo print
    ask_user()
    print(ciphering())
