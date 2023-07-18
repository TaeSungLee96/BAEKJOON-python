a, b, c = map(int, input().split())

ls=[a,b,c]
ls.sort()

result=0
if a==b==c:
    result = 10000 + a*1000
elif a != b and b != c and c != a:
    result = max([a,b,c])*100
elif ls[0]==ls[1]!=ls[2] or ls[0]!=ls[1]==ls[2]:
    result = 1000 + ls[1]*100

print(result)