def divisor(num):
    divisors = [i for i in range(1,num+1) if num%i == 0]

    return divisors

def run():
    try:
        num = int(input('Ingresa un número: '))

        if num > 0:
            print(divisor(num))

            print('Termino el programa')
        else:
            raise TypeError
    except ValueError:
        print('Debes ingresar un número')

    except TypeError:
        print('Debes ingresar un positivo')


if __name__ == '__main__':
    run()