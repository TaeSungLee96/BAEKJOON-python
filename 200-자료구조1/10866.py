from collections import deque

def process_commands(commands):
    result = []
    dq = deque()

    for command in commands:
        if command.startswith('push_front'):
            num = int(command.split()[1])
            dq.appendleft(num)
        elif command.startswith('push_back'):
            num = int(command.split()[1])
            dq.append(num)
        elif command == 'pop_front':
            result.append(dq.popleft() if dq else -1)
        elif command == 'pop_back':
            result.append(dq.pop() if dq else -1)
        elif command == 'size':
            result.append(len(dq))
        elif command == 'empty':
            result.append(0 if dq else 1)
        elif command == 'front':
            result.append(dq[0] if dq else -1)
        elif command == 'back':
            result.append(dq[-1] if dq else -1)

    return result

# 입력 받기
N = int(input())
commands = [input().strip() for _ in range(N)]

# 명령 처리
output = process_commands(commands)

# 출력
for value in output:
    print(value)
