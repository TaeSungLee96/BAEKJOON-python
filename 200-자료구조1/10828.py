import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    input_values = sys.stdin.readline().split()
    order = input_values[0]
    num = input_values[1] if len(input_values) > 1 else None

    if order == "push":
        stack.append(num)
    elif order == "top":
        print(-1) if len(stack) == 0 else print(stack[-1])
    elif order == "pop":
        print(-1) if len(stack) == 0 else print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(1) if len(stack) == 0 else print(0)
