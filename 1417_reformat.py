import collections
import itertools
def reformat(s):
    digit_cnt, letter_cnt = 0, 0
    digits, letters = [], []
    ans = ''
    for ch in s:
        if ch.isdigit():
            digit_cnt += 1
            digits.append(ch)
        elif ch.isalpha():
            letter_cnt += 1
            letters.append(ch)
    
    if 0 <= digit_cnt - letter_cnt <= 1:
        return "".join(itertools.chain.from_iterable(itertools.zip_longest(digits, letters, fillvalue='')))
    elif 0 <= letter_cnt - digit_cnt <= 1:
        return "".join(itertools.chain.from_iterable(itertools.zip_longest(letters, digits, fillvalue='')))
    else:
        return ''

def reformat(self, s: str) -> str:
    letters = [c for c in s if c.isalpha()]
    digits = [c for c in s if c.isdigit()]
    if abs(len(letters) - len(digits)) > 1: return ""
    
    rv = []
    flag = len(letters) > len(digits)
    while letters or digits:
        rv.append(letters.pop() if flag else digits.pop())
        flag = not flag
    return rv


if __name__ == '__main__':
    print(reformat(s = "a0b1c2"))
    print(reformat(s = "covid2019"))