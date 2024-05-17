def check_capture(board, last_move):
    captures = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False] * len(board) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and not visited[i][j]:
                captured_group = bfs(i, j, board, visited)
                if captured_group:
                    captures.append(captured_group)

    if last_move:
        x, y = last_move
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != 0 and not visited[nx][ny]:
                captured_group = bfs(nx, ny, board, visited)
                if captured_group:
                    captures.append(captured_group)

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
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visited[nx][ny]:
                if board[nx][ny] == color:
                    queue.append((nx, ny))
                    group.append((nx, ny))
                    visited[nx][ny] = True
                elif board[nx][ny] == 0:
                    has_liberty = True

    return [] if has_liberty else group