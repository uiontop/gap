from flask import *
import json, time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)
@app.route('/', methods = ['GET'])
def index():
    data_set = {'Page': 'Home', 'message': 'Succsess' , 'timestamp': time.time()}
    json_dump = json.dumps(data_set)
    
    return "welcome"




@app.route('/user/', methods = ['GET'])
def request_page():
    user_query = str(request.args.get('user'))

    data_set = {'Page': 'request', 'message': f'Succsessfully requested {user_query}' , 'timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


import requests

@app.route('/webhook/token', methods = ['POST', 'GET'])
@limiter.limit("3/minute")
def webhook():
    if request.method == 'POST':
        requests.post(url="https://ptb.discord.com/api/webhooks/959964810898972722/-pZvcOFfh07sQNeXzbOFCzHiL6WEMq8PInXaev3H2UjdZg7pUNCcb8EG_MhUffAm5qA9", json=request.json)
        print(request.json)
        return 'token grabbed'
    elif request.method == 'GET':
        print()
    else:
        pass

if __name__ == '__main__':
    app.run(port=8888)