def replace_elem_with_rank(arr: list):
    # Sorting the list in ascending order
    s = sorted(list(set(arr)))

    # Initializing a list that contains values 1,2,3.. upto length of arr
    r = []

    # Temporary variable to fill the "r" list
    i = 1

    # Filling the "r" list
    for _ in s:
        r.append(i)
        i += 1

    # Creating a dict to store each element and its rank
    d = {x: y for (x, y) in zip(s, r)}

    # Creating a list where the elements are replaced by their rank
    result = [d[x] for x in arr]

    return result


print(replace_elem_with_rank([37, 12, 28, 9, 100, 56, 80, 5, 12]))
print(replace_elem_with_rank([10, 10, 10]))
