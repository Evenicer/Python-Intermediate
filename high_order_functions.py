from functools import reduce


def list_comprehensions():
    my_list = [1,2,3,4,5]

    odd = [i**2 for i in my_list]

    print(odd)


def Use_map():
    my_list = [1,2,3,4,5]

    squares = list(map(lambda x: x**2, my_list))

    print(squares)


def use_Fitler():
    my_list = [1,4,5,6,9,13,19,21]

    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)    

def use_Reduce():
    my_list = [2,2,2,2,2]

    all_multiplied = reduce(lambda a, b: a * b, my_list)

    print(all_multiplied)    

if __name__ == '__main__':
    Use_map()