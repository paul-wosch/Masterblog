from flask import Flask
from myapp.config import TEMPLATES_PATH, STATIC_PATH

app = Flask(__name__, template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)