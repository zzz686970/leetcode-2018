def destCity(paths):
    # A, B = map(set, zip(*paths))
    #    return (B - A).pop()
    cityA = set([i[0] for i in paths])
    cityB = set([i[1] for i in paths])
    return list(cityB.difference(cityA))[0]

if __name__ == '__main__':
    print(destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
    print(destCity(paths = [["B","C"],["D","B"],["C","A"]]  ))
    print(destCity(paths = [["A","Z"]]))