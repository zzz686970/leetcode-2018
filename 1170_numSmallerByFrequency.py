import bisect 
import collections
from operator import itemgetter
# >>> c = Counter({'A': 10, 'C':5, 'H':4})
# >>> sorted(c.items(), key=itemgetter(0))
# [('A', 10), ('C', 5), ('H', 4)]
def numSmallerByFrequency(queries, words):
    def f(arr):
        arr = collections.Counter(arr)
        return sorted(arr.items(), key=itemgetter(0))[0][1]
    query_vec = [f(query) for query in queries]
    word_vec = list(sorted([f(word) for word in words]))
    return [len(word_vec) - bisect.bisect(word_vec, query) for query in query_vec]

def numSmallerByFrequency(queries, words):
    f = sorted(w.count(min(w)) for w in words)
    return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]

def numSmallerByFrequency(queries, words):
    f = lambda x: x.count(min(x))
    words = sorted([f(w) for w in words])
    return [len(words) - bisect(words,f(q)) for q in queries]

if __name__ == '__main__':
    print(numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
    print(numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))