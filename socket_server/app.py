from flask import Flask, render_template,request,Response
from flask_socketio import SocketIO
import json
import requests
from pymongo import MongoClient
from datetime import datetime,timedelta
import socketio as sio_client

# import ssl
# import ipdb

app = Flask(__name__)
app.secret_key = "sfdjkafnk"

# context = ssl.SSLContext(ssl.PROTOCOL_TLS)



socketio = SocketIO(app, cors_allowed_origins="*")
# socketio = SocketIO(app)
client = MongoClient('mongodb+srv://demo:esoft1234@cluster0-9vwrc.azure.mongodb.net/test?retryWrites=true&w=majority')
#client = MongoClient('mongodb+srv://amit:adspv3445k123@cluster0-pos-dev1-pri.trimn.mongodb.net/POS_DEV?retryWrites=true&w=majority')
db = client.POS
sio = sio_client.Client()

# ipdb.set_trace()
@app.route('/')
def test():
    return render_template('index.html')

@app.route("/device_code", methods=['POST'])
def device_code():

    url = "https://connect.squareup.com/v2/devices/codes"
    data = json.loads(request.data.decode('utf-8'))
    db_response = db.test_devices_web.insert_one({
                                "device_id":data['device_code']['name'],
                                })
    headers = {
        'Authorization': "Bearer EAAAEMP6hHCBw8DzJOLaBys0jS32ahwsfEiFdF8OZMlx4shYX5IYomqWIu2wgO1w",
        # 'Authorization': "Bearer EAAAEBAw2nXOHmFHxS09oNkGXza5_EqidQGAe4Q6UglDs9F0cwrJsFgvVxqoegzS",
        'Content-Type': "application/json"
        }
    response = requests.request("POST", url, data=json.dumps(data), headers=headers).text
    return Response(json.dumps({"meta":{"code":"200","message" : "SUCCESS"},"data":json.loads(response)}),mimetype='application/json')

@app.route("/device_pair/<device_code>", methods=['GET'])
def device_pair(device_code):
    url = "https://connect.squareup.com/v2/devices/codes/{0}".format(device_code)
    headers = {
        'Authorization': "Bearer EAAAEMP6hHCBw8DzJOLaBys0jS32ahwsfEiFdF8OZMlx4shYX5IYomqWIu2wgO1w",
        'Content-Type': "application/json"
        }

    response = json.loads(requests.request("GET", url, headers=headers).text)
    if response['device_code']['status']=="PAIRED":
        db.pos_terminal_device_id.update_one(
                                {"device_id":response['device_code']['name']},
                                {"$set":{
                                "terminal_id":response['device_code']['device_id']    
                                # "updated_date":dateutil.parser.parse(datetime.now(timezone('US/Eastern')).strftime("%m-%d-%Y %H:%M:%S"))
                                }})
    return Response(json.dumps({"meta":{"code":"200","message" : "SUCCESS"},"data":response}),mimetype='application/json')

@app.route("/checkout_create",methods=['POST'])
def checkout_create():
    url = "https://connect.squareup.com/v2/terminals/checkouts"

    data = json.loads(request.data.decode('utf-8'))
    print("Data@@@", data)
    app.logger.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@post data@@@@@@@@@@@@@@@@@@")
    app.logger.info(data)
    app.logger.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@post data@@@@@@@@@@@@@@@@@@")
    headers = {
        'Authorization': "Bearer EAAAEMP6hHCBw8DzJOLaBys0jS32ahwsfEiFdF8OZMlx4shYX5IYomqWIu2wgO1w",
        'Content-Type': "application/json",
        }
    response = requests.request("POST", url, data=json.dumps(data), headers=headers).text
    app.logger.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@resposne data@@@@@@@@@@@@@@@@@@")
    app.logger.info(json.loads(response))
    app.logger.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@resposne data@@@@@@@@@@@@@@@@@@")
    return Response(json.dumps({"meta":{"code":"200","message" : "SUCCESS"},"data":json.loads(response)}),mimetype='application/json')


@socketio.on('checkout_response',namespace='/square_terminal')
# @socketio.on('checkout_response')
def handle_checkout_response_event(data):
    # print("data@@@",data)
    # print("device_id@@@@@",data['checkout']['reference_id'])
    print("device_id@@@@@", data['data']['object']['checkout']['note'])
    # device_data = db.pos_terminal_device_id.find_one({"device_id":int(data['reference_id']),"terminal_id":data['device_options']['device_id'],"conectivity_status":"PAIRED"})
    # data = {"checkout":json.dumps({"message":data})}
    # namesapce_id = "/{0}".format(device_data['device_id'])
    #nameapce_reference_id = "/{0}".format(data['checkout']['reference_id'])
    # nameapce_reference_id = 5219
    nameapce_reference_id = "/{0}".format(data['data']['object']['checkout']['note'])
    namesapce_id = "/{0}".format(data['data']['object']['checkout']['device_options']['device_id'])
    # namesapce_id = "/{0}".format(data['checkout']['device_options']['device_id'])
    app.logger.info(namesapce_id)
    app.logger.info("@@@@@@@@@@@@@this is data from client@@@@@@@@@@@@@")
    app.logger.info(data)
    app.logger.info("@@@@@@@@@@@@@this is data from client@@@@@@@@@@@@@")
    # socketio.emit('checkout_response',data, namespace=namesapce_id)
    socketio.emit('checkout_response_send', data, namespace=nameapce_reference_id)
    # socketio.emit('checkout_response', data)
    print("socket.emit@@@@@")



if __name__ == '__main__':
    # certfile = os.path.join(ROOT_DIR, 'private/cert.pem')
    # keyfile = os.path.join(ROOT_DIR, 'private/privkey.pem')
    # socketio.run(app,host='10.10.16.199',port=6000,debug=True)
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)

