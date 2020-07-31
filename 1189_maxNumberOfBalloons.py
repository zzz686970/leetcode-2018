import collections
def maxNumberOfBalloons(text):
    cnt = collections.Counter(text)
    res = []
    for key, val in cnt.items():
        if key in map(str, 'ban'):
            res.append(val)
        elif key in map(str, 'lo'):
            res.append(val // 2)
    return min(res) if len(res) == 5 else 0

    # cntBalloon = collections.Counter('balloon')
    # return min([cnt[c] // cntBalloon[c] for c in cntBalloon])

if __name__ == '__main__':
    print(maxNumberOfBalloons(text = "nlaebolko"))
    print(maxNumberOfBalloons(text = "loonbalxballpoon"))
    print(maxNumberOfBalloons(text = "leetcode"))