import flask
import os

BE_addr = os.environ.get('BE_addr',"localhost:10001")


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", BE_addr = BE_addr)



@app.route("/health")
def healthCheck():
    return """
200 OK
    """



if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')