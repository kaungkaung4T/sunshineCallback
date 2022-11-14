from flask import Flask, request, Response


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    return "wef"

@app.route('/work', methods=['GET'])
def work():
    return "work"


if __name__ == "__main__":
    app.run()
