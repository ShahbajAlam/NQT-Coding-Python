def non_repeating(a: str):
    result = ""

    for i in a:
        if a.count(i) == 1:
            result += i

    return result


print(non_repeating("shahbaj"))
