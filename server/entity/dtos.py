

class GameData:
    def __init__(self, board, white_captured, black_captured, current_turn):
        self.board = board  
        self.white_captured = white_captured  
        self.black_captured = black_captured  
        self.current_turn = current_turn
        
    def scored(self):
        def dfs_recursive(x, y):
            # Đánh dấu vị trí hiện tại là đã thăm
            self.visited[x][y] = True
            self.count = self.count + 1
            # Duyệt các ô liền kề
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    # nếu là ô trống chưa thăm -> thăm
                    if self.board[nx][ny] is None and not self.visited[nx][ny]:
                        dfs_recursive(nx, ny)
                    # là ô đen hoặc trắng. nếu là lãnh thổ vô chủ 
                    elif self.flag == 'either':
                        continue
                    # nếu là ô đen
                    elif self.board[nx][ny] == 'black':
                        self.flag = 'black' if self.flag != 'white' else 'either'
                    # nếu là ô trắng
                    elif self.board[nx][ny] == 'white':
                        self.flag = 'white' if self.flag != 'black' else 'either'
        
        # khởi tạo ma trận đánh dấu
        self.visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                # duyệt ô trống chưa duyệt
                if self.board[x][y] is None and not self.visited[x][y]:
                    # gắn cờ phân loại lãnh thổ của ai
                    self.flag = None
                    # đếm số ô lãnh thổ
                    self.count = 0
                    # duyệt theo chiều sâu tìm lãnh thổ
                    dfs_recursive(x, y)
                    # xử lý: nếu lãnh thổ của quân đen -> cộng điểm quân đen
                    if (self.flag == 'black'):
                        self.black_scored = self.black_scored + self.count
                    # xử lý: nếu lãnh thổ của quân trắng -> cộng điểm quân trắng
                    elif (self.flag == 'white'):
                        self.white_scored = self.white_scored + self.count
                    # bỏ qua nếu lãnh thổ vô chủ     
        return self.black_scored, self.white_scored + 6.5