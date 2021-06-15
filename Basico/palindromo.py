def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")

    try:
        es_palindromo = palindromo(palabra)

        if es_palindromo:
            print('Es palíndromo')
        else:
            print('No es palíndromo')
    except TypeError:
        print('Solo se pueden ingresar strings')


if __name__ == '__main__':
    run()