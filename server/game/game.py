class GoGame:
    def __init__(self, size=19):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.current_player = 'black'
        self.pass_flag = None
        self.black_scored = 0
        self.white_scored = 0
        self.mode = 'friend'

    def pass_turn(self, color): # bo qua luot
        if (self.current_player != color):
            return None
        if (self.pass_flag != None): # neu bo qua lien tiep
            return False # ket thuc game
        self.pass_flag = self.current_player
        self.current_player = 'white' if self.current_player == 'black' else 'black' 
        return True

    def place_stone(self, board, captured_count, color):
        if (self.current_player != color):
            return False
        self.previous_board = self.board
        self.board = board
        self.pass_flag = None
        if self.current_player == 'black':
            self.black_scored = self.black_scored + captured_count
            self.current_player = 'white'  
        else:
            self.white_scored = self.white_scored + captured_count
            self.current_player = 'black'
        return True

        
    def place_stone(self, x, y, color):
        def check_liberties(x, y):
            # Kiểm tra các ô kề cạnh
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    # Nếu ô trống
                    if self.board[nx][ny] is None:
                        return True
                    # Nếu là ô quân đồng minh
                    elif self.board[nx][ny] == self.current_player:
                        if self.check_liberties(nx, ny):
                            return True
            return False
        
        # Kiểm tra lượt chơi
        if (self.current_player != color):
            return False
        # Kiểm tra ô có trống không
        if self.board[x][y] is not None:
            return False        
        # Kiểm tra ô có khí không
        if not check_liberties(x, y):
            return False
        
        # Đặt quân cờ
        self.previous_board = self.board
        self.board[x][y] = self.current_player
        self.current_player = 'white' if self.current_player == 'black' else 'black'
        self.pass_flag = None
    
        # kiem tra lanh tho
        # code here
        return True
    
    def get_board(self):
        return self.board

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
    
    def get_game_state(self):
        return {
            'board': self.board,
            'white_captured': self.black_scored,
            'black_captured': self.white_scored,
            'current_turn': self.current_turn,
        }