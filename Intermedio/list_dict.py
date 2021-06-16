def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'jasel', 'lastname': 'lee'} 

    super_list = [
        {'firstname': 'jasel', 'lastname': 'lee'} ,
        {'firstname': 'andrea', 'lastname': 'enciso'} ,
        {'firstname': 'alex', 'lastname': 'enciso'} ,
        {'firstname': 'jessica', 'lastname': 'gonzalez'} ,
        {'firstname': 'mayra', 'lastname': 'contreras'} ,
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,-3,4,-5],
        "float_nums": [4.5,6.7,1.2,3.3]
    }

    for i in super_list:
        print(i.items())


if __name__ == '__main__':
    run()