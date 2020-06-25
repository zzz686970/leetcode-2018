def distanceBetweenBusStops(distance, start, destination):
    if start > destination:
        start, destination = destination, start

    # return min(sum(distance[start:destination]), sum(distance[destination:]) + sum(distance[:start]))
    return min(sum(distance[start:destination]), sum(distance) - sum(distance[start:destination]))

if __name__ == '__main__':
    print(distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
    print(distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
    print(distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))
    print(distanceBetweenBusStops(distance = [7,10,1,12,11,14,5,0], start = 7, destination = 2))