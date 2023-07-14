N = int(input())

x_ls = []
y_ls = []

if N != 1:
    for _ in range(N):
        x, y = map(int, input().split())
        x_ls.append(x)
        y_ls.append(y)
    print((max(x_ls)-min(x_ls))*(max(y_ls)-min(y_ls)))
else:
    print(0)