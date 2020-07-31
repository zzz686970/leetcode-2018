def numWaterBottles(numBottles: int, numExchange: int) -> int:
    ans = numBottles
    while numBottles >= numExchange:
        ans += numBottles // numExchange
        numBottles = numBottles //  numExchange + numBottles % numExchange

    return ans 


if __name__ == '__main__':
    print(numWaterBottles(numBottles = 15, numExchange = 4))
    print(numWaterBottles(numBottles = 5, numExchange = 5))
    print(numWaterBottles(numBottles = 2, numExchange = 3))