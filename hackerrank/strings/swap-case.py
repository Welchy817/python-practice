def swap_case(s):
    swap = ""
    for i in s:
        if i.isupper():
            swap = swap + i.lower()
        else:
            swap = swap + i.upper()
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)