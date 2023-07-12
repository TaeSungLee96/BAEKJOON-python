x = int(input())
a = 0
b = 0

for i in range(1, x + 1):  # 1부터 x + 1까지
    if a >= x:  # 만약 a가 x보다 작거나 같으면
        break  # break
    a += i  # a = a + i를 하고,
    b += 1  # b를 증감

if b % 2 != 1:  # b 나누기 2가 짝수이면
    print(b - (a - x), '/', a - x + 1, sep='')

elif b % 2 == 1:  # b 나누기 2가 홀수이면
    print(a - x + 1, '/', b - (a - x), sep='')