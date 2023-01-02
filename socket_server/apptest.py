from flask import Flask
from flask import json
from flask import request
# from flask_ngrok import run_with_ngrok


app = Flask(__name__)
# run_with_ngrok(app)


@app.route('/')
def call():
    return 'Good Morning'

@app.route('/github' , methods=['POST'])
def for_square():
    if request.headers['content-type'] == 'application/json':
        my_info = json.dumps(request.json)
        print(my_info)
        return my_info


if __name__ == '__main__':
    app.run(debug=True)