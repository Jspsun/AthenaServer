from flask import Flask, json, request
app = Flask(__name__)

# http://127.0.0.1:5000/


@app.route('/', methods=['POST'])
def api_root():

    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "Unsuported request. Please post a JSON"


if __name__ == '__main__':
    app.run()
