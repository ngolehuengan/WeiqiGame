def check_capture(board, last_move):
    captures = []
    # visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    visited = [[False] * len(board) for _ in range(len(board))]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and not visited[i][j]:
                captured_group = bfs(i, j, board, visited)
                captures.extend(captured_group)

    if last_move:
        x, y = last_move
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                nx >= 0
                and ny >= 0
                and nx < len(board)
                and ny < len(board)
                and board[nx][ny] != 0
                and not visited[nx][ny]
            ):
                captured_group = bfs(nx, ny, board, visited)
                captures.extend(captured_group)

    return captures


def bfs(x, y, board, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    color = board[x][y]
    queue = [(x, y)]
    group = [(x, y)]
    visited[x][y] = True
    has_liberty = False

    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (
                nx >= 0
                and ny >= 0
                and nx < len(board)
                and ny < len(board)
                and not visited[nx][ny]
            ):
                if board[nx][ny] == color:
                    queue.append((nx, ny))
                    group.append((nx, ny))
                    visited[nx][ny] = True
                elif board[nx][ny] == 0:
                    has_liberty = True

    return [] if has_liberty else group

def is_valid_capture_move(boardCellsArray, isBlackTurn, captures, clicked_square_coordinates):
    global iskoMove, koPoint
    
    colors = []
    for element in captures:
        x = element[0]
        y = element[1]
        color = boardCellsArray[x][y]
        colors.append(color)
    
    all_captured_same_color = all(color == colors[0] for color in colors)
    self_capture = (isBlackTurn and colors[0] == 1) or (not isBlackTurn and colors[0] == 2)
    
    if all_captured_same_color and self_capture:
        return False
    
    turn = 1 if isBlackTurn else 2
    
    if not all_captured_same_color and iskoMove and clicked_square_coordinates[0] == koPoint[0] and clicked_square_coordinates[1] == koPoint[1]:
        return False
    
    iskoMove = not all_captured_same_color
    
    for element in captures:
        if turn != boardCellsArray[element[0]][element[1]]:
            clicked_square_coordinates = element
    
    koPoint = clicked_square_coordinates if iskoMove else [-1, 1]
    
    return True

# def remove_piece(x, y):
#     square_id = str(x) + str(y)
#     square = document.getElementById(square_id)
#     children = square.childNodes
#     for i in range(len(children) - 1, -1, -1):
#         if not children[i].classList.contains(styles.line) and not children[i].classList.contains(styles.star):
#             square.removeChild(children[i])