n = int(input())
for k in range(n):
    a = [str(i + 1) for i in range(n)]
    if k % 2 == 1:
        a.reverse()
    b = ''.join(a)
    print(b)