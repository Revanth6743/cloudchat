from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace_with_a_secret'   # for production, use an env variable
socketio = SocketIO(app, cors_allowed_origins="*")   # allow all origins for dev

@app.route('/')
def home():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    print(f"{data['user']}: {data['text']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    # For local dev only; production will use gunicorn + eventlet
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
