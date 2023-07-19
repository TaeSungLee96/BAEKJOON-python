def is_valid_parenthesis(string):
    stack = []  # 스택을 저장할 리스트

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어있는 경우
                return False
            stack.pop()

    if stack:  # 스택이 비어있지 않은 경우
        return False
    else:
        return True


t = int(input())  # 테스트 데이터 수 입력

for _ in range(t):
    test_string = input()  # 괄호 문자열 입력

    if is_valid_parenthesis(test_string):
        print("YES")
    else:
        print("NO")
