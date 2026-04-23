N = int(input("N: "))

board = [[0]*N for _ in range(N)]

# Branch & Bound arrays
row = [0]*N
ld = [0]*(2*N)
rd = [0]*(2*N)


def solve(col):
    if col >= N:
        return True

    for i in range(N):

        # Bounding condition (O(1) check)
        if row[i] == 0 and ld[i - col + N] == 0 and rd[i + col] == 0:

            board[i][col] = 1
            row[i] = 1
            ld[i - col + N] = 1
            rd[i + col] = 1

            if solve(col + 1):
                return True

            # Backtrack
            board[i][col] = 0
            row[i] = 0
            ld[i - col + N] = 0
            rd[i + col] = 0

    return False


if solve(0):
    print("Solution:")
    for r in board:
        print(r)
else:
    print("No Solution")