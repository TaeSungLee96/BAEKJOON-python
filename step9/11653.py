import math

def prime_factors(n):
    factors = []

    # 2로 나눌 수 있는 만큼 나누기
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 3부터 제곱근까지의 홀수로 나누기
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # 남은 수가 소수인 경우 추가
    if n > 2:
        factors.append(n)

    return factors

num = int(input())
factors = prime_factors(num)
for f in factors:
    print(f)
