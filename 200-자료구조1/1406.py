import sys

def p(ls, string, cursor_idx):
    ls.insert(cursor_idx, string)
    return cursor_idx+1

def b(ls, cursor_idx):
    if cursor_idx == 0:
        return cursor_idx
    elif cursor_idx >= len(ls):
        del ls[len(string)-1]
        return cursor_idx - 1
    else:
        del ls[cursor_idx-1]
        return cursor_idx - 1

def d(cursor_idx, string):
    if cursor_idx == -1:
        return len(string)
    else:
        return cursor_idx + 1

def l(cursor_idx):
    if cursor_idx == 0:
        return 0
    else:
        return cursor_idx - 1

string = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())

cursor_index = len(string)

for i in range(m):
    ls = list(map(str, sys.stdin.readline().rstrip().split()))

    order = ls[0]
    word = ls[1] if len(ls) > 1 else None

    if order == "P":
        cursor_index = p(string, word, cursor_index)
        # print(string, cursor_index, "PPP")
    elif order == "L":
        cursor_index = l(cursor_index)
        # print(string, cursor_index, "LLL")
    elif order == "B":
        cursor_index = b(string, cursor_index)
        # print(string, cursor_index, "BBB")
    elif order == "D":
        cursor_index = d(cursor_index, string)
        # print(string, cursor_index, "DDD")
    else:
        string.append(order)
        # print(string, cursor_index, "HAHA")

print("".join(string))