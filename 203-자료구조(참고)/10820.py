while True:
    try:
        s = input()
        up, down, num, void = 0, 0, 0, 0

        for alpha in s:
            if alpha.isupper():
                up += 1
            elif alpha.islower():
                down += 1
            elif alpha.isdigit():
                num += 1
            elif alpha == " ":
                void += 1
        print(down, up, num, void)
    except EOFError:
        break
