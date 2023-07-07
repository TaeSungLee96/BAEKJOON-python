T = int(input())
R, S = "", ""


for a in range(T):
    R, S = map(str, input().split())
    result = ""
    for s in list(S):
        result += s * int(R)
    print(result)