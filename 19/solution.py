def equlibrium_index(arr: list):
    for i in range(len(arr)):
        index = i

        if sum(arr[:index]) == sum(arr[(index + 1) :]):
            return index


arr = [-7, 1, 5, 2, -4, 3, 0]

print(equlibrium_index(arr))
