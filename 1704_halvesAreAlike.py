from itertools import accumulate

def halvesAreAlike(s):
    return sum((s[i] in set('aeiouAEIOU')) - (s[-i-1] in set('aeiouAEIOU')) for i in range(len(s)//2)) == 0
    return sum(map(lambda x: 1 if x.lower() in 'aeiou' else 0, s[:len(s)//2])) == sum(map(lambda x: 1 if x.lower() in 'aeiou' else 0, s[len(s)//2:]))


    # return list(map(lambda x: 1 if x.lower() in 'aeiou' else 0, s[:len(s)//2], s[len(s)//2:]))

if __name__ == '__main__':
    print(halvesAreAlike("book"))