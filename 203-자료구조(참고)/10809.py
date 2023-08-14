word = input()  # 단어 입력
alphabet_count = [-1] * 26  # 알파벳 개수를 저장할 리스트 초기화

for char in word:
    alphabet_count[ord(char) - ord('a')] = word.index(char)

# 결과 출력
for count in alphabet_count:
    print(count, end=' ')
