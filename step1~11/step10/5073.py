while True:
    a, b, c = map(int, input().split())
    sort_ls = sorted([a, b, c])
    sort_ls_cp = sorted([a, b, c])

    if a == b == c == 0:
        break

    if a == b == c:
        print("Equilateral")
    else:
        sort_ls_cp.remove(max(a, b, c))
        if max(a, b, c) >= sum(sort_ls_cp):
            print("Invalid")
        elif sort_ls[0] == sort_ls[1] != sort_ls[2] or sort_ls[0] != sort_ls[1] == sort_ls[2]:
            print("Isosceles")
        elif a != b != c:
            print("Scalene")

