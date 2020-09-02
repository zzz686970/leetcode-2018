def thousandSeparator(n):
    s = ""
    for i, val in enumerate(reversed(str(n)), 1):
        s += val
        if i % 3 == 0 and i < len(str(n)):
            s += '.'

    return "".join(list(reversed(s)))

    # return f"{n:,}".replace(",", ".")

if __name__ == '__main__':
    print(thousandSeparator(987))
    print(thousandSeparator(1234))
    print(thousandSeparator(123456789))
    print(thousandSeparator(0))