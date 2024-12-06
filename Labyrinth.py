from collections import deque

temp = input()
temp = temp.split()
n = int(temp[0])
m = int(temp[1])

maze = [list(input()) for _ in range(n)]
bookmark = [[(0, 0) for _ in range(m)] for _ in range(n)]

A = (0, 0)
B = (0, 0)

for j in range(n):
    for i in range(m):
        if maze[j][i] == "A":
            A = (j, i)
        elif maze[j][i] == "B":
            B = (j, i)
            
def bfs(start_j, start_i):
    queue = deque([(start_j, start_i)])  # Use deque instead of list
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    while queue:
        curr = queue.popleft()  # O(1) pop from the front
        j, i = curr
        for dj, di in dirs:
            nj, ni = j + dj, i + di
            if (0 <= ni < m) and (0 <= nj < n) and ((maze[nj][ni] == ".") or (maze[nj][ni] == "B")) and (bookmark[nj][ni] == (0, 0)):
                bookmark[nj][ni] = (-dj, -di)
                if (nj, ni) == B:
                    return True
                queue.append((nj, ni))
    return False

if bfs(A[0], A[1]):
    print("YES")
    backtrack = 0
    j, i = B
    seq = []
    while (j, i) != A:
        backtrack += 1
        if bookmark[j][i] == (-1, 0):
            seq.append("D")
        elif bookmark[j][i] == (0, -1):
            seq.append("R")
        elif bookmark[j][i] == (1, 0):
            seq.append("U")
        elif bookmark[j][i] == (0, 1):
            seq.append("L")
        j, i = j + bookmark[j][i][0], i + bookmark[j][i][1]
    print(backtrack)
    print("".join(reversed(seq)))
else:
    print("NO")
