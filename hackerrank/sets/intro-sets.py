def average(array):
    # your code goes here
    arrSum = 0
    for num in set(array):
        arrSum += num
    return arrSum / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)