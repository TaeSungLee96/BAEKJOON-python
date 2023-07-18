word = input()

ls = []
if len(word) == 1:
    print(1)
else:
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            print(0)
            break
        else:
            ls.append(1)
    if sum(ls) == len(word)//2:
        print(1)