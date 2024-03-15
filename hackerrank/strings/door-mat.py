# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split(" "))
for i in range(n):
    dash = abs(int(((m-3)/2) - ((i)*3)))
    middle = int((m/2)-3)
    top_design = 2 * i + 1
    bot_design = 2 * (n-i) - 1
    if i < int(((n-1)/2)):
        print(("-" * dash) + (".|." * top_design) + ("-" * dash))
    elif i == (int(((n-1)/2))):
        print(("-" * middle) + "WELCOME" + ("-" * middle))
    else:
        print(("-" * dash) + (".|." * bot_design) + ("-" * dash))