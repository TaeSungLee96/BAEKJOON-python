import sys
from collections import deque

# 공백도 들어가야함
str = sys.stdin.readline().strip()
str = deque(list(str))
l = len(str)
flag = False

st = []
while l > 0:
    if str[0] == '<':
        while st:
            str.append(st.pop())
        str.append(str.popleft())
        flag = True

    elif str[0] == ' ':
        while st:
            str.append(st.pop())
        str.append(str.popleft())

    elif str[0] == '>':
        str.append(str.popleft())
        flag = False
    else:
        if flag == True:
            str.append(str.popleft())

        else:
            st.append(str.popleft())
    l -= 1

while st:
    str.append(st.pop())
print(''.join(str))
