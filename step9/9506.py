while True:
    a = int(input())

    if a == -1:
        break
    i = 1
    result = ""
    for _ in range(a):
        if a == i:
            break
        if a % i == 0:
            result += f"{str(i)} + "

        i += 1
    total = sum(map(int, [n.replace(" ", "") for n in result[:-2].split("+")]))

    if a == total:
        print(f"{a} = {result[:-2]}")
    else:
        print(f"{a} is NOT perfect.")