from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", "r") as f:
        return f.read()

@app.route("/test", methods=["GET"])
def test():
    input_data = request.args.get('heads')
    response = requests.post("http://backend-listener-2:7070", headers={
        "Access-Control-Allow-Origin": "*"
    }, json={"heads": input_data})
    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
