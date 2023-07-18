paper=[[0]*100 for _ in range(100)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for x_axis in range(x, x + 10):
        for y_axis in range(y, y + 10):
            paper[y_axis][x_axis] = 1

cnt = 0
for i in range(100):
    cnt += paper[i].count(1)

print(cnt)