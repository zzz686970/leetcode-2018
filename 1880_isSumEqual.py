def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    # numeric_total = lambda s: int(''.join([str(ord(letter) - ord('a')) for letter in s]))
    # return numeric_total(firstWord) + numeric_total(secondWord) == numeric_total(targetWord)

    dic = dict(zip('abcdefghij', range(10)))
    first = "".join(map(lambda x: str(dic[x]), firstWord))
    second = "".join(map(lambda x: str(dic[x]), secondWord))
    target = "".join(map(lambda x: str(dic[x]), targetWord))
    return int(first) + int(second) == int(target)

if __name__ == '__main__':
    isSumEqual('j', 'j', 'bi')