word = input()  # 단어 입력
alphabet_count = [0] * 26  # 알파벳 개수를 저장할 리스트 초기화

for char in word:
    # 알파벳이면 해당 알파벳의 인덱스에 1 추가
    if char.isalpha():
        alphabet_count[ord(char) - ord('a')] += 1

# 결과 출력
for count in alphabet_count:
    print(count, end=' ')
