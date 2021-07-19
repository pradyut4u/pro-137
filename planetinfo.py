from flask import Flask
from flask import jsonify
from flask import request
from planetdata import data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "data":data,
        "message":"message"
    }),200

@app.route("/search")
def search():
    name = request.args.get("name")
    planetdata = next(item for item in data if item["name"] == name)
    return jsonify({
        "planetdata":planetdata,
        "message":"message"
    }),200

@app.route("/planettype")
def planettype():
    name = request.args.get("ptype")
    planetname = [i for i in data if i["ptype"] == ptype]
    return planetname
    return jsonify({
        "planetname":planetname,
        "message":"message"
    }),200

if __name__ == "__main__":
    app.run()