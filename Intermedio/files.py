def read():
    numbers = []

    with open('/Users/jasel/Documents/Python/Python/Intermedio/files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    
    print(numbers)


def write():
    names = ['Jasel','Andrea','Mayra','Jessica','Ofelia','Rocío']

    with open('/Users/jasel/Documents/Python/Python/Intermedio/files/names.txt', 'w', encoding='utf-8') as f:
        for n in names:
            f.write(n)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()