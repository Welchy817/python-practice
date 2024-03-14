if __name__ == '__main__':
    n = int(input().strip())
    if 6 <= n <= 20:
        print("Weird")
    elif n%2 == 0:
        print("Not Weird")
    else:
        print("Weird")
