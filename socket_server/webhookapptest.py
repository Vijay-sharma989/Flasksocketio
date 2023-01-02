from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# @socketio.on('message',namespace='/chat')
@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    # send(data,broadcast=True)

@socketio.on('message_user', namespace='/chat')
def handle_message_qw(message):
    message="qwfyeeytr"
    send(message)


if __name__ == '__main__':
    socketio.run(app,debug=True)
#
# from flask import Flask
# from flask_socketio import SocketIO, send
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecret'
# socketio = SocketIO(app, cors_allowed_origins='*')
#
# @socketio.on('message')
# def handleMessage(msg):
# 	print('Message: ' + msg)
# 	send(msg, broadcast=True)
#
# if __name__ == '__main__':
# 	socketio.run(app)