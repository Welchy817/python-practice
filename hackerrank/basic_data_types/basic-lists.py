if __name__ == '__main__':
    aList = []
    N = int(input())
    for _ in range(N):
        op = input().split()
        if "insert" in op[0]:
            aList.insert(int(op[1]), int(op[2]))
        elif "print" in op[0]:
            print(aList)
        elif "remove" in op[0]:
            aList.remove(int(op[1]))
        elif "append" in op[0]:
            aList.append(int(op[1]))
        elif "sort" in op[0]:
            aList.sort()
        elif "pop" in op[0]:
            aList.pop()
        elif "reverse" in op[0]:
            aList.reverse()