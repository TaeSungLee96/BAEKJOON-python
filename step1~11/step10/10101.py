a = int(input())
b = int(input())
c = int(input())

sort_ls = sorted([a, b, c])


if a == b == c == 60:
    print("Equilateral")
elif a+b+c == 180 and (sort_ls[0] == sort_ls[1] != sort_ls[2] or sort_ls[0] != sort_ls[1] == sort_ls[2]):
    print("Isosceles")
elif a+b+c == 180 and a != b != c:
    print("Scalene")
elif a+b+c != 180:
    print("Error")
