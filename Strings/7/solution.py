def reverse(a: str):
    l = list(a)
    l.reverse()
    return "".join(l)


print(reverse("abcd1234"))
