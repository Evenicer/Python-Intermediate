from math import sqrt


def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # print(my_dict)    

    #Dictionary Comprehension con llave los primeros 100 numeros y valor el numero al cubo solo los que sean divisibles entre 3
    #my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    #Dictionary Comprehension con llave los primeros 1000 numeros y valor cada numero al cuadrado
    my_dict = {i: round(sqrt(i)) for i in range(1, 1001)}

    print(my_dict)
    

if __name__ == '__main__':
    run()