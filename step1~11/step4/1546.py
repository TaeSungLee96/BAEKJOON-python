N = int(input())
ls = list(map(int, input().split()))
max_num = max(ls)
new_ls = []
for el in ls:
    new_ls.append(el/max_num*100)
print(sum(new_ls)/len(new_ls))
