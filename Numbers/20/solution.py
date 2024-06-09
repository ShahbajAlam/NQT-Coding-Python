def is_automorphic_number(num: int):
    square = str(int(num**2))
    length_of_the_num = len(str(num))

    return num == int(square[-length_of_the_num:])


print(is_automorphic_number(76))
