def left_rotate(arr: list, k: int):
    for _ in range(k):
        first_item = arr.pop(0)
        arr.append(first_item)
    return arr


def right_rotate(arr: list, k: int):
    for _ in range(k):
        last_item = arr.pop()
        arr.insert(0, last_item)
    return arr


print(left_rotate([10, 20, 30, 40, 50, 60], 3))
print(right_rotate([10, 20, 30, 40, 50, 60], 1))
