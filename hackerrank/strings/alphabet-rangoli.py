def print_rangoli(size):
    # your code goes here
    alphabet = [chr(i) for i in range(ord('a'), ord('a') + size)]
    for i in reversed(range(len(alphabet))):
        string1 = alphabet[i:size]
        string2 = alphabet[i+1:size][::-1]
        rangoli1 = string2 + string1
        if i == size - 1:
            print("-".join(string1).center((size*4) - 3, "-"))
        else:
            print("-".join(rangoli1).center((size*4) - 3, "-"))
    for j in range(len(alphabet) - 1):
        string3 = alphabet[j+1:size]
        string4 = alphabet[j+2:size][::-1]
        rangoli2 = string4 + string3
        print("-".join(rangoli2).center((size*4) - 3, "-"))