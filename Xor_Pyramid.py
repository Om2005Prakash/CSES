n = int(input())
base = input()

base = [int(i) for i in base.split()]

power2s = 0
res = base[0]

for i in range(1,n):
    temp = (n-i)
    while(temp % 2 == 0):
        power2s += 1
        temp /= 2
    temp = i
    while(temp %2 == 0):
        power2s -= 1
        temp /= 2
    if power2s == 0:
        res = res^base[i]
print(res)