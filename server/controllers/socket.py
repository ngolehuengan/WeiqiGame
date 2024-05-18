from flask_socketio import emit, join_room, leave_room
from main import socketio
from game.game import GoGame
import uuid

games = {}

@socketio.on('create_game')
def handle_create_game(data):
    size = data.get('size', 19)
    game_id = str(uuid.uuid4())  # Tạo một ID duy nhất cho ván chơi
    games[game_id] = GoGame(size)
    join_room(game_id)  # Người tạo tham gia vào phòng
    emit('game_created', {'game_id': game_id, 'game_state': games[game_id].get_game_state()}, room=game_id)

@socketio.on('join_game')
def handle_join_game(data):
    game_id = data['game_id']
    if game_id in games:
        join_room(game_id)  # Người chơi thứ hai tham gia vào phòng
        emit('game_joined', {'game_id': game_id, 'game_state': games[game_id].get_game_state()}, room=game_id)
    else:
        emit('error', {'message': 'Game not found'})

@socketio.on('quit_game')
def handle_quit_game(data):
    game_id = data['game_id']
    if game_id in games:
        leave_room(game_id)
        if len(games[game_id].players) == 0: # Nếu không còn người chơi trong ván chơi
            del games[game_id] # Loại bỏ ván chơi khỏi danh sách
    else:
        emit('error', {'message': 'Game not found'})

@socketio.on('place_stone')
def handle_place_stone(data):
    game_id = data['game_id']
    if game_id in games:
        board, captured_count, color = data['board'], data['captured_count'], data['color']
        games[game_id].place_stone(board, captured_count, color)
        emit('stone_placed', {'game_state': games[game_id].get_game_state()}, room=game_id)
    else:
        emit('error', {'message': 'Game not found'})

@socketio.on('pass_turn')
def handle_pass_turn(data):
    game_id = data['game_id']
    if game_id in games:
        color = data['color']
        rs = games[game_id].pass_turn(color)
        
        if rs is not None:
            if rs: 
                emit('turn_passed', {'game_state': games[game_id].get_game_state()}, room=game_id)
            else:
                handle_score(data)
    else:
        emit('error', {'message': 'Game not found'})

@socketio.on('score')
def handle_score(data):
    game_id = data['game_id']
    if game_id in games:
        b_score, w_score = games[game_id].score()
        emit('scored', {'score': {b_score, w_score}}, room=game_id)
    else:
        emit('error', {'message': 'Game not found'})
        