from flask import Flask, url_for
app = Flask(__name__)

# http://127.0.0.1:5000/


@app.route('/<message>')
def api_root(message):
    return message


if __name__ == '__main__':
    app.run()
