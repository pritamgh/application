from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Testing after 2 months, Date: 09-04-2025"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)