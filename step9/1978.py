N = int(input())

ls = list(map(int, input().split()))

result = 0
for number in ls:
    if number == 1:
        continue
    p = 0
    for i in range(2, number):
        if number % i != 0:
            p += 1
    if p == number-2:
        result += 1

print(result)