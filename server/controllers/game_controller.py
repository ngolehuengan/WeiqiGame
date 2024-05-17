from flask import Blueprint, jsonify, request, make_response
from services.game1 import check_capture

captures_bp = Blueprint('check_captures', __name__)

@captures_bp.route('/api/check_captures', methods=['OPTIONS'])
def options_check_captures():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

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
