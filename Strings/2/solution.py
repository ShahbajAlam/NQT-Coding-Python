def count(a: str):
    a = a.lower()
    vowels = 0
    consonants = 0
    spaces = 0

    for i in a:
        if i == " ":
            spaces += 1
        if i in "aeiou":
            vowels += 1
        if i in "bcdfghjklmnpqrstvwxyz":
            consonants += 1

    return vowels, consonants, spaces


print(count("I am shahbaj alam....."))
