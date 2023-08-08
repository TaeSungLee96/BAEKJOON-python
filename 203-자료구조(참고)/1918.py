def infix_to_postfix(expression):
    # 연산자의 우선순위를 정의합니다.
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    result = []  # 변환된 후위 표기식을 저장할 리스트
    stack = []   # 연산자를 임시로 저장할 스택

    for char in expression:
        if char.isalpha():  # 알파벳이면 피연산자이므로 결과 리스트에 추가합니다.
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # '('를 스택에서 제거
        else:  # 연산자일 경우
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(char)

    # 스택에 남아있는 연산자들을 결과 리스트에 추가합니다.
    while stack:
        result.append(stack.pop())

    return ''.join(result)

# 입력을 받고 후위 표기식으로 변환한 결과를 출력합니다.
infix_expression = input()
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)
