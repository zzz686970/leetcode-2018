def minFlips(self, a: int, b: int, c: int) -> int:
    max_len = len(bin(max(a,b,c))[2:])
    a, b, c = map(lambda x: [int(el) for el in bin(x)[2:].zfill(max_len)], [a,b,c])
    cnt = 0
    for x, y, z in zip(a, b, c):
        if x | y != z:
            if x & y == 1:
                cnt += 2
            else:
                cnt += 1
    return cnt

    # return 0 if a==b==c==0 else self.minFlips(a >> 1, b>>1, c>>1) + (not (a%2 or b%2) if c%2 else (a%2 + b%2))