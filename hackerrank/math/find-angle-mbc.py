# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, asin, degrees

degree_sign = u'\N{DEGREE SIGN}'

AB = int(input())
BC = int(input())
AC = sqrt((pow(AB, 2) + pow(BC, 2)))
MC = AC/2
MBC = round(degrees(asin(AB/AC)))
print(f"{MBC}{degree_sign}")