import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        idx = stack.pop()
        result[idx] = a[i]
    stack.append(i)

answer = " ".join(map(str, result))
print(answer)
