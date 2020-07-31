import itertools
def maxPower(s):
    print(list([a, list(b)] for a, b in itertools.groupby(s)))
    dp = [1 for _ in range(len(s))]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dp[i] += dp[i-1]
            
    return max(dp)

    # return max(len(list(b)) for a, b in itertools.groupby(s))


if __name__ == '__main__':
    print(maxPower(s = "leetcode"))
    print(maxPower(s = "abbcccddddeeeeedcba"))
    print(maxPower(s = "triplepillooooow"))
    print(maxPower(s = "hooraaaaaaaaaaay"))
    print(maxPower(s = "tourist"))