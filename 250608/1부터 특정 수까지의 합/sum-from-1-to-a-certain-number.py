n = int(input())

# Please write your code here. ㅇㅇ 알겟슴
def sum_10(n):
    sum = 0
    for i in range(n+1):
        sum += i
    a = sum//10
    return a

answer = sum_10(n)
print(answer)