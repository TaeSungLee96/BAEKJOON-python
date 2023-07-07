A, B = map(str, input().split())
rev_A = int("".join(reversed(A)))
rev_B = int("".join(reversed(B)))

print(rev_A if rev_A>rev_B else rev_B)
