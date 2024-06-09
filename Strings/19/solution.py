def lasrgest_word(sentence: str):
    words = sentence.split()
    words = sorted(words, reverse=True, key=len)
    return words[0]


print(lasrgest_word("my name is shahbaj alam, an engineering student"))
