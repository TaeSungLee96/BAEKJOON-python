N, M = map(int,(input().split()))

bucket = list(range(1,N+1))
for n in range(M):
    i,j = map(int, input().split())

    temp = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = temp

print(" ".join(str(s) for s in bucket))
