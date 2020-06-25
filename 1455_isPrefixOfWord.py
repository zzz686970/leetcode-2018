def isPrefixOfWord(sentence, searchWord):
    for idx, word in enumerate(sentence.split(' ')):
        if word.startswith(searchWord):
            return idx + 1  

    return -1 

    ## one line
    # return next(((i + 1) for (i, word) in enumerate(sentence.split()) if word.startswith(searchWord)), -1)

if __name__ == '__main__':
    print(isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
    print(isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro"))
    print(isPrefixOfWord(sentence = "i am tired", searchWord = "you"))
    print(isPrefixOfWord(sentence = "i use triple pillow", searchWord = "pill"))
    print(isPrefixOfWord(sentence = "hello from the other side", searchWord = "they"))
    print(isPrefixOfWord(sentence = "hellohello hellohellohello", searchWord = "ell"))