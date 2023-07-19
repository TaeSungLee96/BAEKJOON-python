initial_string = list(input())
left_list = initial_string
right_list = []
cursor_index = len(left_list)

command_count = int(input())

for _ in range(command_count):
    command = input().split()

    if command[0] == "L":
        if left_list:
            right_list.append(left_list.pop())
            cursor_index -= 1
    elif command[0] == "D":
        if right_list:
            left_list.append(right_list.pop())
            cursor_index += 1
    elif command[0] == "B":
        if left_list:
            left_list.pop()
            cursor_index -= 1
    elif command[0] == "P":
        left_list.append(command[1])
        cursor_index += 1

final_string = ''.join(left_list + right_list)
print(final_string)
