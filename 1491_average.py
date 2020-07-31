import math
def average(salary):
    min_s, max_s = math.inf, -math.inf
    result = 0
    for s in salary:
        min_s = min(min_s, s)
        max_s = max(max_s, s)
        result += s 

    return (result - min_s - max_s) / (len(salary)-2)




