def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Rogelio","lastname": "Valle"}

    super_list = [ 
        {"firstname": "Rogelio","lastname": "Valle"},
        {"firstname": "Evenicer","lastname": "Robles"},
        {"firstname": "Esme","lastname": "Morquecho"},
        {"firstname": "Cillian","lastname": "Murphy"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 3.3, 5.5]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for i in super_list:
        print(i)    

if __name__ == '__main__':
    run()