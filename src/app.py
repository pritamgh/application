from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return """Committing from my PC. CI/CD pipeline is working fine. Hurray!!"""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)