N, M = map(int,(input().split()))

bucket = [0]*N
for n in range(M):
    i,j,k = map(int, input().split())
    bucket[i-1:j] = [k]*(j-i+1)
print(" ".join(str(s) for s in bucket))
