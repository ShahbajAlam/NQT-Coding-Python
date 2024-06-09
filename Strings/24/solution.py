def helper(word: str):
    result = ""

    for i in reversed(word):
        result += i

    return result


def reverse_words(sentence: str):
    words = sentence.split()
    result = []

    for word in words:
        result.append(helper(word))

    return " ".join(result)


print(reverse_words("my name is shahbaj alam"))
