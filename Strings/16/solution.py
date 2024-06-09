def print_duplicates(a: str):
    duplicates = ""

    for i in a:
        if a.count(i) > 1 and i not in duplicates:
            duplicates += i

    print(duplicates)


print_duplicates("shahbaj")
