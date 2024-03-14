if __name__ == '__main__':
    n = int(input())
    lists = input().split(" ")
    tup = tuple(map(int, lists))
    print(hash(tup))