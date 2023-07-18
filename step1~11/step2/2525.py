a, b = map(int, input().split())
c = int(input())

plus_h = int(c/60)
plus_m = c%60

a +=plus_h
b +=plus_m
if b >= 60:
    a+=int(b/60)
    b=int(b%60)

if a >= 24:
    a%= 24
print(a, b)