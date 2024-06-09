def remove_vowels(a: str):
    result = ""

    for i in a:
        if i not in "aeiouAEIOU":
            result += i

    return result


print(remove_vowels("shahbaj alam"))
