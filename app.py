import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Hello This is Our Group 2"


app.run()
