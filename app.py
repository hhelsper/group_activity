import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    """Returns root endpoint HTML"""

    return "hey"


app.run()
