# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(input())

ordered = OrderedDict()
for items in range(N):
    price = 0
    item_name = ""
    item = list(map(str, input().split()))
    item_name = ' '.join(item[0:len(item)-1])
    price = int(item[len(item)-1])
    if item_name in ordered.keys():
        ordered[item_name] += price
    else:
        ordered[item_name] = price
    
for grocery, net in ordered.items():
    print(f"{grocery} {net}")