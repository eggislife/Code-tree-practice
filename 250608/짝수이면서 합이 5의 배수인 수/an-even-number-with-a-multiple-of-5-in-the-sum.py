n = int(input())

# Please write your code here. ㅇㅋ

n = str(n)
def hwook(n):
    if int(n)%2==0 and (int(n[0])+int(n[1]))%5 == 0:
        print('Yes')
    else:
        print('No')

hwook(n)