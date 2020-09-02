def coinChange(coins, amount):
    coins.sort()
    cnt = 0
    while amount >= 0 and coins:
        largest = coins.pop()
        while amount >= largest:
            amount -= largest
            cnt += 1

    return cnt if amount == 0 else -1

if __name__ == '__main__':
    print(coinChange(coins = [2], amount = 3))
    print(coinChange(coins = [1, 2, 5], amount = 11))

