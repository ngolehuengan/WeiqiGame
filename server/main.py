import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from controllers.login_controller import login_bp
from controllers.game_controller import captures_bp

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, origins="http://localhost:3000")

app.register_blueprint(login_bp)
app.register_blueprint(captures_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    socketio.run(app, debug=True)