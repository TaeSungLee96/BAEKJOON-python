import sys
n = int(sys.stdin.readline())
queue = []

for i in range(n):
    input_values = sys.stdin.readline().split()
    order = input_values[0]
    num = input_values[1] if len(input_values) > 1 else None

    if order == "push":
        queue.append(num)
    elif order == "front":
        print(-1) if len(queue) == 0 else print(queue[0])
    elif order == "back":
        print(-1) if len(queue) == 0 else print(queue[-1])
    elif order == "pop":
        print(-1) if len(queue) == 0 else print(queue.pop(0))
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        print(1) if len(queue) == 0 else print(0)
