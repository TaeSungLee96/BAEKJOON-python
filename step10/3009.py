x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x_ls = sorted([x1, x2, x3])
y_ls = sorted([y1, y2, y3])

result = ""
if x_ls[0] == x_ls[1]:
    result += str(x_ls[2])
else:
    result += str(x_ls[0])

if y_ls[0] == y_ls[1]:
    result += f" {y_ls[2]}"
else:
    result += f" {y_ls[0]}"

print(result)

