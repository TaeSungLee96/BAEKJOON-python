def count_pieces(s):
    stack = []
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:  # s[i] == ')'
            stack.pop()
            if s[i - 1] == '(':
                count += len(stack)
            else:
                count += 1
    return count

print(count_pieces(input().strip()))
