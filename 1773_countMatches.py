from typing import List
def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    li = {'type':0, 'color':1, 'name':2}
    return sum(map(lambda x: x[li[ruleKey]] == ruleValue, items))
    # return sum(1 for item in items if item[self.li[ruleKey]] == ruleValue)

if __name__ == '__main__':
    print(countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
    print(countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))