from flask import Blueprint, jsonify, request
from services.login_service import get_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/api/login', methods=['POST'])
def login():
    try:
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return jsonify({'success': False, 'message': 'Vui lòng nhập đầy đủ tên người dùng và mật khẩu'}), 200

            user, error = get_user(username, password)
            if error:
                return jsonify({'success': False, 'message': error}), 500

            if user:
                return jsonify({'success': True, 'message': 'Đăng nhập thành công!'}), 200
            else:
                return jsonify({'success': False, 'message': 'Tài khoản hoặc mật khẩu không chính xác.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Yêu cầu không phải là JSON.'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': 'Lỗi không xác định.', 'details': str(e)}), 500
