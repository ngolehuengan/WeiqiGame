from flask import Blueprint, jsonify, request, make_response
from services.game1 import check_capture

captures_bp = Blueprint('check_captures', __name__)

@captures_bp.route('/api/check_captures', methods=['POST'])
def check_captures():
    try:
        if request.is_json:
            data = request.get_json()
            board = data.get('board')
            last_move = data.get('last_move')

            if board is None or last_move is None:
                return jsonify({'success': False, 'message': 'Vui lòng cung cấp đầy đủ dữ liệu bảng và nước đi cuối'}), 400

            captures = check_capture(board, last_move)

            if captures:
                return jsonify({'success': True, 'captures': captures, 'message': 'Thành công'}), 200
            else:
                return jsonify({'success': False, 'message': 'Không có bắt quân.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Yêu cầu không phải là JSON.'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': 'Lỗi không xác định.', 'details': str(e)}), 500
    
    
captures_valid = Blueprint('is_valid_capture_move', __name__)

@captures_valid.route('/api/is_valid_capture_move', methods=['POST'])
def is_valid_capture_move():
    try:
        data = request.get_json()
        boardCellsArray = data.get('boardCellsArray')
        isBlackTurn = data.get('isBlackTurn')
        captures = data.get('captures')
        clicked_square_coordinates = data.get('clicked_square_coordinates')
        
        # Kiểm tra xem dữ liệu đầu vào có hợp lệ không
        if not captures or not clicked_square_coordinates:
            return jsonify({'success': False, 'message': 'Vui lòng cung cấp dữ liệu hợp lệ.'}), 400

        # Gọi hàm kiểm tra từ module hoặc service
        is_valid = is_valid_capture_move(boardCellsArray, isBlackTurn, captures, clicked_square_coordinates)
        
        # Trả về kết quả
        return jsonify({'success': True, 'is_valid': is_valid}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': 'Lỗi không xác định.', 'details': str(e)}), 500
