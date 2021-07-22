from collections import defaultdict
class TimeMap():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ans = defaultdict(dict)
        self.prev_time = -1
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ans[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ans:
            return ''
        else:
            
            
            for k, v in self.ans[key].items():

                if timestamp >= k:
                    self.prev_time = max(k, self.prev_time)
                    print(self.self.prev_time)
            return self.ans[key].get(self.prev_time, '')

# Your TimeMap object will be instantiated and called as such:
timeMap =  TimeMap()
print(timeMap.set("foo", "bar", 1))  ## store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         ## return "bar"
print(timeMap.get("foo", 3))         ## return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
print(timeMap.set("foo", "bar2", 4)) ## store the key "foo" and value "ba2r" along with timestamp = 4.
print(timeMap.get("foo", 4))         ## return "bar2"
print(timeMap.get("foo", 5))         ## return "bar2"

