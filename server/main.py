import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from flask import Flask
from flask_cors import CORS
from controllers.login_controller import login_bp

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)