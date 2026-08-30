def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]

        if placed == col:
            return False

        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]


def display_board(solution, n):
    for row in range(n):
        print(" ".join("Q" if solution[row] == col else "." 
                       for col in range(n)))


# Solve for N = 5, 7 and 9
for n in [5, 7, 9]:
    solutions, backtracks = solve_n_queens(n)

    print(f"N={n}: {len(solutions)} solutions, {backtracks} backtracks")

    if n == 5:
        print("One solution:")
        display_board(solutions[0], n)
