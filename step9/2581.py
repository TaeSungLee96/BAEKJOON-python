import math

M = int(input())
N = int(input())

is_prime = [True] * (N+1)  # 소수 판별 결과를 저장할 배열

# 에라토스테네스의 체 알고리즘을 이용하여 소수 판별
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i*2, N+1, i):
            is_prime[j] = False

result = []
for number in range(M, N+1):
    if is_prime[number]:
        result.append(number)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
