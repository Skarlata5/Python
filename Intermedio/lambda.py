def run():
    palindorme = lambda string: string == string[::-1]

    try:
        print(palindorme('ana'))
    except TypeError:
        print('Solo se pueden ingresar strings')


if __name__ == '__main__':
    run()