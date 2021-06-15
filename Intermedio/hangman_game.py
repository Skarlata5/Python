import random
import os

def read():
    data = []

    with open('/Users/jasel/Documents/Python/Python/Intermedio/files/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.upper())

    return data[random.randint(1, len(data))]


def hide_word(str):
    result = ''
    for s in str:
        result += "_ "

    return result

def find_char(str, c, hide):
    status = ''
    hide = hide.replace(' ','')

    for i in range(len(str)):
        if str[i] == c:
            status += c
        elif hide[i] != '_':
            status +=hide[i]
        else:
            status += "_ "

    return status


def run():
    os.system ("clear")
    print('¡Adivina la palabra!')
    word =  read().replace('\n','')
    hide = hide_word(word)
    print(hide_word(word))

    char = input('\nIngresa una letra:')
    status = find_char(word, char.upper(), hide)

    while(word != status):
        os.system ("clear")
        print('¡Adivina la palabra!')
        print(status)   
        
        char = input('\nIngresa una letra:')
        status = find_char(word, char.upper(), status)
    
    print('¡Ganaste la palabra es: ' + word + '!')








if __name__ == '__main__':
    run()