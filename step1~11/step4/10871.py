N, X = map(int, input().split())
ls = list(map(int, input().split()))

result = ""
for n in ls:
    if n < X:
        result += str(n)+" "
print(result)