n = int(input())
for k in range(n):
    for i in range(n):
        if i % 2 == 0:
            print(k + 1, end = '')
        else:
            print(n - k, end = '')
    print()