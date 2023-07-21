def josephus(n, k):
    result = []
    idx = 0
    ls = list(range(1, n + 1))

    for i in range(n, 0, -1):
        idx = (idx + k - 1) % len(ls)
        result.append(ls.pop(idx))

    return result

n, k = map(int, input().split())
josephus_sequence = josephus(n, k)
result_str = ", ".join(str(x) for x in josephus_sequence)
print(f"<{result_str}>")
