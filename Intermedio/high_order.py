from functools import reduce

def run():
    #filter
    my_list = [1,3,4,5,6,9,13,19,22]
    odd = list(filter(lambda x: x%2 != 0,my_list))

    print(odd)

    #map
    my_map = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_map))

    print(squares)

    #reduce
    my_reduce = [2,2,2,2,2] 

    all_multiplied = reduce(lambda a,b: a*b, my_reduce)

    print(all_multiplied)



if __name__ == '__main__':
    run()