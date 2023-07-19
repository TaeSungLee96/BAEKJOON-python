n = int(input())  # 수열의 길이를 입력받음

stack = []  # 스택을 저장할 리스트
result = []  # push와 pop 연산을 저장할 리스트
count = 1  # 1부터 n까지의 숫자를 차례로 확인하기 위한 변수

for _ in range(n):
    num = int(input())  # 수열의 숫자를 입력받음
    while count <= num:  # 현재 숫자가 스택에 들어갈 때까지 push 연산 수행
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == num:  # 스택의 top과 현재 숫자가 일치하는 경우 pop 연산 수행
        stack.pop()
        result.append('-')
    else:  # 일치하지 않는 경우 주어진 수열을 만들 수 없음
        print('NO')
        exit(0)

for op in result:  # 수행된 연산 출력
    print(op)
