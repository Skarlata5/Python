def divisor(num):
    divisors = [i for i in range(1,num+1) if num%i == 0]

    return divisors

def run():

    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'Debes ingresar un número'

    print(divisor(int(num)))

    print('Termino el programa')


if __name__ == '__main__':
    run()