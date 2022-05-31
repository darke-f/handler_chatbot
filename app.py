from flask import Flask, render_template, request, jsonify
from chats import get_response, predict_class

app = Flask(__name__)

@app.get("/")

def index_get():
    return render_template("base.html")

@app.post("/answer")

def predict():
    text = request.get_json().get("message")

    ints = predict_class(text)
    response = get_response(ints)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run()