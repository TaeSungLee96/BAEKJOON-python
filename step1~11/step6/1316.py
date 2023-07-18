cnt = 0
n = input()

for i in range(int(n)):
    a = list(input())
    p = 0
    if len(set(a)) == 1:
        cnt += 1
        continue
    for x in range(len(a)-2):
        if a[x] in a[x+2:] and a[x+1] != a[x]:
            p += 1
    if p == 0:
        cnt += 1
print(cnt)
