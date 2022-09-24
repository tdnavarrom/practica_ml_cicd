import flask
from main import predict_handler


app = flask.Flask("CloudFunction")


@app.route("/", methods=["POST"])
def predict():
    return predict_handler(flask.request)


app.run()
