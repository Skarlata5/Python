import random
import string

def generar_contrasena():
    mayusculas = list(string.ascii_uppercase)
    minusculas = list(string.ascii_lowercase)
    simbolos = ['!','@','#','$','%','&','/','(',')','=']
    numeros = ['0','1','2','3','4','5','6','7','8','9']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        char_random =  random.choice(caracteres)
        contrasena.append(char_random)

    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)

if __name__ == '__main__':
    run()