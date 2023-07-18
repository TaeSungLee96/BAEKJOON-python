n = int(input())

for i in range(n):
    word_origin = input().split()
    word = [word + " " for word in word_origin]

    result = ""
    for s in word:
        result += s[::-1]
    print(result.strip())