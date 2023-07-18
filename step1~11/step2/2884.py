a, b = map(int, input().split())
min = b-45

if min < 0:
    a-=1
    b=60+min
    if a<0:
        a+=24
else:
    b=min
print(a, b)