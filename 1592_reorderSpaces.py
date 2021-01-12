def reorderSpaces(text: str) -> str:
    cnt = text.count(' ')
    text_list = text.split(' ')
    total_pair = len([el for el in text_list if el]) -1
    res = []
    if cnt == 0: return text
    if total_pair == 0: return text.strip() + " " * cnt
    for el in text_list:
        if el:
            res.append(el)
            res.extend([' ' * (cnt // total_pair)])
    res.pop()
    if cnt % total_pair:
        res.extend([' ' * (cnt % total_pair)])

    return "".join(res)

if __name__ == '__main__':
    print(reorderSpaces("  this   is  a sentence "))
    print(reorderSpaces("a"))
    print(reorderSpaces("  hello"))
    print(reorderSpaces("   a"))
                