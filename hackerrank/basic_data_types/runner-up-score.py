if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    firstPlace = -100
    secondPlace = int()
    for i in scores:
        if i > firstPlace:
            secondPlace = firstPlace
            firstPlace = i
        elif firstPlace > i > secondPlace:
            secondPlace = i
    print(secondPlace)