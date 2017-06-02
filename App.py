from flask import Flask, json, request
import os
# from flask_rest_service import app
app = Flask(__name__)

# http://127.0.0.1:5000/


@app.route('/', methods=['POST'])
def api_root():

    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "Unsuported request. Please post a JSON"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
