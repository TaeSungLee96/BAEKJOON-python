S = input()

result = ""
for i in range(97, 123):
    result += f'{S.find(chr(i))} '
print(result)

