ls = []
max_num = 0
max_row = 1
max_col = 1
for i in range(9):
    ls = list(map(int, input().split()))
    if max_num < max(ls):
        max_num = max(ls)
        max_row = i+1
        max_col = ls.index(max_num) + 1
print(max_num)
print(max_row, max_col)