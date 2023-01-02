from flask import Flask, render_template,request,Response
import json
import requests
from datetime import datetime,timedelta
import socketio as sio_client


app = Flask(__name__)
app.secret_key = "sfdjkafnk"
sio = sio_client.Client()
sio.connect('http://127.0.0.1:5000', namespaces=['/square_terminal'])
# sio.connect('https://pos.esoftech.in:443', namespaces=['/square_terminal'])

print(sio)
@app.route('/checkout_create_webhook', methods=['POST'])
def checkout_create_webhook():
    try:
        data = json.loads(request.data.decode('utf-8'))
        app.logger.info("@@@@@@@@@@@@@webhook response@@@@@@@@@@@@@")
        app.logger.info(data)
        app.logger.info("@@@@@@@@@@@@@webhook response@@@@@@@@@@@@@")
        print("ekeflhef;le@")
        sio.emit('checkout_response',data, namespace='/square_terminal')
        # sio.emit('checkout_response', data)
        print("sio_print@@@@@@@")
        return Response(json.dumps({"meta":{"code":"200","message" : "SUCCESS"},"data":data}),mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'meta': {"code": "500", 'message': 'Error'}, 'data': str(e)}), status=500,
                        mimetype='application/json')
                        




if __name__ == '__main__':
    app.run(host='127.0.0.1',port=6000,debug=True)
