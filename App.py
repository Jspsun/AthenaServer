from flask import Flask, json, request
import os
import Config

app = Flask(__name__)

# http://127.0.0.1:5000/


@app.route('/', methods=['Post'])
def api_root():
    # validate that user sends in a json
    if request.headers['Content-Type'] != 'application/json':
        return "Please post a JSON"

    data = json.loads(json.dumps(request.json))

    # validate that JSON has all the needed parameters (Message)
    if not('Authenication' in data and "Message" in data):
        return "Please send a JSON with valid data"

    # validate that authenication token is correct
    if data['Authenication'] != Config.Authentication:
        return "Incorrect authentication"

    return "Hi " + Config.Authentication


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(debug=True, host='localhost', port=port)
