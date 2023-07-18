N, B = input().split()
num_dict = {}
for i in range(10,36):
    num_dict[i] = chr(i+55)

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod in list(num_dict.keys()):
            rev_base += num_dict[mod]
        else:
            rev_base += str(mod)

    return rev_base[::-1]

print(solution(int(N), int(B)))