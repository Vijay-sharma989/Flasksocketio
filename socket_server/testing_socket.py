from flask import Flask, render_template,request,Response
from flask_socketio import SocketIO
import json
import requests
from pymongo import MongoClient
from datetime import datetime,timedelta
import socketio as sio_client


app = Flask(__name__)
app.secret_key = "sfdjkafnk"
sio = sio_client.Client()

sio.connect('https://774f-202-166-184-2.in.ngrok.io')
# sio.connect('http://13.234.154.194:5000')
print(sio)
# socketio = SocketIO(app)


@sio.on('checkout_response')
def handle_tst_checkout_response_event(data):
    print("data@@@",data)
    app.logger.info("@@@@@@@@@@@@@this is data from client@@@@@@@@@@@@@")
    app.logger.info(data)
    app.logger.info("@@@@@@@@@@@@@this is data from client@@@@@@@@@@@@@")


if __name__ == '__main__':
    # certfile = os.path.join(ROOT_DIR, 'private/cert.pem')
    # keyfile = os.path.join(ROOT_DIR, 'private/privkey.pem')
    # socketio.run(app,host='10.10.16.199',port=6000,debug=True)
    # socketio.run(app, host='127.0.0.1', port=8000, debug=True)
    app.run('127.0.0.1', port=8000, debug=True)