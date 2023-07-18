a, b = map(int, input().split())

i=1
ls=[]
while True:
    if a % i == 0:
        ls.append(i)
    if a == i:
        break
    i+=1
try:
    print(ls[b-1])
except:
    print(0)