from collections import Counter


def anagram1(a: str, b: str):
    return sorted(a) == sorted(b)


def anagram2(a: str, b: str):
    return Counter(a) == Counter(b)


print(anagram1("listen", "silent"))
print(anagram2("listen", "silent"))
