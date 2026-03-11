n = int(input())

col = [False] * n
diag1 = [False] * (2 * n - 1)   # row + col
diag2 = [False] * (2 * n - 1)   # row - col + n - 1

count = 0

def dfs(row):
    global count

    if row == n:
        count += 1
        return

    for c in range(n):
        if col[c] or diag1[row + c] or diag2[row - c + n - 1]:
            continue

        col[c] = True
        diag1[row + c] = True
        diag2[row - c + n - 1] = True

        dfs(row + 1)

        col[c] = False
        diag1[row + c] = False
        diag2[row - c + n - 1] = False

dfs(0)
print(count)