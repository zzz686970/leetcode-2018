def finalPrices(prices):
    res = []
    for idx, price in enumerate(prices):
        for j in range(idx+1, len(prices)):
            if price >= prices[j]:
                res.append(price-prices[j])
                break
        else:
            res.append(price)
    
    return res

def finalPrices(self, prices):
    stack = []
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
        stack.append(idx)
    
    return prices

