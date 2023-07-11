ls_1 = input()
ls_2 = input()
ls_3 = input()
ls_4 = input()
ls_5 = input()

max_length = max(len(ls_1), len(ls_2),len(ls_3),len(ls_4),len(ls_5))
result = ""
for i in range(max_length):
    if i < len(ls_1):
        result += ls_1[i]
    if i < len(ls_2):
        result += ls_2[i]
    if i < len(ls_3):
        result += ls_3[i]
    if i < len(ls_4):
        result += ls_4[i]
    if i < len(ls_5):
        result += ls_5[i]
print(result)