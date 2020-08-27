def maxScore(s: str) -> int:
    ## one pass 
    zeroes = 1 if s[0] == '0' else 0
    ## count from index 1
    ones = s.count('1', 1)
    scores = zeroes + ones
    for i in range(1, len(s) - 1):
        if s[i] == '0':
            zeroes += 1
        else:
            ones -= 1
        
        scores = max(zeroes + ones, scores)
    
    return scores

