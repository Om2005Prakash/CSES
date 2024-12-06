n, tar = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
count = 0
i = 0
j = 0
sum = arr[i]
while(j <= n):
    if (i > j):
        j += 1
        sum += (0 if (j >= n) else arr[j])
    elif sum > tar:
        sum -= arr[i]
        i += 1
    elif sum < tar:
        j += 1
        sum += (0 if (j >= n) else arr[j])
    else:
        count += 1
        sum -= arr[i]
        i += 1
print(count)