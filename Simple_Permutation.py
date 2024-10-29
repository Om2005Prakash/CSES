for i in range(int(input())):
    n = int(input())
    data = [int(j) for j in input().split()]
    indx = {elem:i for i,elem in enumerate(data)}
    res = 0
    for j in range(n):
        if (data[j] != -1) and (data[j] != j+1):
            if data[data[j] - 1] == j+1:
                data[data[j] - 1] = -1
            else:
                data[indx[j + 1]] = data[data[j] - 1]
                indx[data[data[j] - 1]] = indx[j + 1]
                data[data[j] - 1] = -1
                res += 1
    print(res)