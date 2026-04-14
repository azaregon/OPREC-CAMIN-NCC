import flask
import json
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/addname", methods=['POST'])
def addName():
    nametoadd  = flask.request.json.get("nama")

    msg_to_return = {"code": 200, "msg": "OK"}

    with open('namedb.json','r') as namedb:
        
        namedb_dict = json.load(namedb)
        if nametoadd not in namedb_dict:
            namedb_dict[nametoadd] = 1
        else:
            msg_to_return = {"code": 409, "msg": "data has already recorded"}
            # print("has already added")

    with open('namedb.json','w') as namedb:
        json.dump(namedb_dict,namedb)

    return flask.jsonify(msg_to_return), msg_to_return['code']

@app.route("/health")
def healthCheck():
    return """
200 OK
    """

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')