try:
    with open("happy1.txt", mode="x") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("File does not exist")
    raise err
except IOError as err:
    print("Issue with performing an IO operation")
    # raise err

