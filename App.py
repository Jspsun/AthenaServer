from flask import Flask, json, request
from CommandHandler import CommandCenter
import os
import Config

app = Flask(__name__)

# Post a json to flask server
# Requires:
#   {
#   Authentication: INSERT AUTH CODE
#   ClientType: TYPE OF DEVICE
#   Message : CONTENT TO PARSE
#   }


@app.route('/', methods=['Post'])
def api_root():
    # validate that user sends in a json
    if request.headers['Content-Type'] != 'application/json':
        return "Please post a JSON"

    data = json.loads(json.dumps(request.json))

    # validate that JSON has all the needed parameters (Message)
    if not('Authenication' in data and "ClientType" in data and "Message" in data):
        return "Please send a JSON with valid data"

    # validate that authenication token is correct
    if data['Authenication'] != Config.Authentication:
        return "Incorrect authentication"

    # Pass data to command center
    CommandCenter.process(data['Message'])

    return "Hi " + Config.Authentication


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(debug=True, host='0.0.0.0', port=port)
