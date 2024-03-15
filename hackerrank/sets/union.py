# Enter your code here. Read input from STDIN. Print output to STDOUT
engNum = int(input())
engStudent = set(map(int, input().split()))
freNum = int(input())
freStudent = set(map(int, input().split()))
print(len(engStudent.union(freStudent)))