s = input()

result = ""

for w in s:
    if w.isupper():
        n = ord(w)
        n += 13
        if n > 90:
            n %= 90
            n += 64
        result += chr(n)
    elif w.islower():
        n = ord(w)
        n += 13
        if n > 122:
            n %= 122
            n += 96
        result += chr(n)
    elif w == " ":
        result += w
    else:
        result += w

print(result)