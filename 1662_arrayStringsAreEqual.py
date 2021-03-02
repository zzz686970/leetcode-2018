def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return all(a == b for a, b in zip (Counter(sorted("".join(word1))).items(), Counter(sorted("".join(word2))).items()))

if __name__ == '__main__':
	print(arrayStringsAreEqual(["jbboxe","yshcrtanrtlzyyp","vudsssnzuef","lde"],
["jbboxeyshcrtanrt","lzyypvudsssnzueflde"]))

	print(["a", "cb"], ["ab", "c"])