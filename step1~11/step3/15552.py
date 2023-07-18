import sys

a=int(input())

for i in range(a):
    c,d=map(int,sys.stdin.readline().split())
    print(c+d)