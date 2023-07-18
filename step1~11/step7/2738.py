N, M = map(int, input().split())

ls1 = []
for i in range(N):
     ls1.append((input().split()))

ls2 = []
for j in range(N):
     ls2.append((input().split()))

for k in range(len(ls1)):
    bucket = [int(x)+int(y) for x, y in zip(ls1[k], ls2[k])]
    print(" ".join(str(s) for s in bucket))
