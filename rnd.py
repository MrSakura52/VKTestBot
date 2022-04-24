def valid_solution(board):
    for i in range(0, len(board), 3):
        for i2 in range(0, len(board[i]), 3):
            values = []
            for i3 in range(i, i + 3):
                for i4 in range(i2, i2 + 3):
                    if board[i3][i4] in values or board[i3][i4] == 0:
                        print(i, i2, i3, i4)
                        return False
                    values.append(board[i3][i4])
    else: return True
print(valid_solution([
[1, 3, 2, 5, 7, 9, 4, 6, 8], 
[4, 9, 8, 2, 6, 0, 3, 7, 5], 
[7, 0, 6, 3, 8, 0, 2, 1, 9], 
[6, 4, 3, 1, 5, 0, 7, 9, 2], 
[5, 2, 1, 7, 9, 0, 8, 4, 6], 
[9, 8, 0, 4, 2, 6, 5, 3, 1], 
[2, 1, 4, 9, 3, 5, 6, 8, 7], 
[3, 6, 0, 8, 1, 7, 9, 2, 4], 
[8, 7, 0, 6, 4, 2, 1, 3, 5]]))