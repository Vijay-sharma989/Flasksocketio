# from socketIO_client import SocketIO, LoggingNamespace


# socketIO = SocketIO('127.0.0.1', 5000, LoggingNamespace)
# # socketIO.on('response', test_response)
# data = {
#             "id": "7qsiSPr06QqqO",
#             "amount_money": {
#                 "amount": 100,
#                 "currency": "USD"
#             },
#             "reference_id": "123456",
#             "note": "Test Note",
#             "device_options": {
#                 "device_id": "Q99Z9TQYVVCM3",
#                 "tip_settings": {
#                     "allow_tipping": False
#                 },
#                 "skip_receipt_screen": False
#             },
#             "status": "PENDING",
#             "created_at": "2020-08-17T11:45:58.129Z",
#             "updated_at": "2020-08-17T11:45:58.129Z",
#             "app_id": "sq0idp-_GTUMmpZp_4sTMd-hNyzVw",
#             "deadline_duration": "PT5M",
#             "payment_type": "CARD_PRESENT"
#         }
# room = "test_room"
# #join_room(room)
# socketIO.emit('checkout_response',data)
# socketIO.wait(seconds=1)

import socketio


sio = socketio.Client()

sio.connect('http://e70983f48a7e.ngrok.io', namespaces=['/square_terminal'])


# sio.emit('checkout_response', {'foo': 'bar'}, namespace='/square_terminal')
