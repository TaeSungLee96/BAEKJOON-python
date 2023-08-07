def calculate_postfix(expression, operands):
    stack = []
    for token in expression:
        if token.isalpha():  # 피연산자인 경우
            stack.append(operands[ord(token) - ord('A')])  # 해당 피연산자에 대응하는 값을 스택에 넣습니다.
        else:  # 연산자인 경우
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack[0]  # 스택에는 계산 결과만 남아 있으므로, 그 값을 반환합니다.

# 입력 받기
N = int(input())
expression = input().strip()
operands = []
for _ in range(N):
    operands.append(int(input()))

result = calculate_postfix(expression, operands)
print("{:.2f}".format(result))  # 결과를 소숫점 둘째 자리까지 출력합니다.
