div_num = 0
result = 0
p_cnt = 0
for _ in range(20):
    name, score, grade = input().split()
    obj = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
    if grade != "P":
        result += float(score) * obj[grade]
        div_num += float(score)


print(result/div_num)