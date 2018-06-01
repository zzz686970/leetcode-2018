def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    result = []
    tmp = []
    a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    b = 'abcdefghijklmnopqrstuvwxyz'
    for word in words:
        result.append([dict(zip(b, a))[char] for char in word ])

    for sub in result:
        y = "".join(x for x in sub)
        tmp.append("".join(y))

    return len(set(tmp))

words = ["gin", "zen", "gig", "msg"]

print(uniqueMorseRepresentations(words))