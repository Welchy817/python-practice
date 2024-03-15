def minion_game(string):
    # your code goes here
    count = kevin = stuart = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)
        count+=1
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)