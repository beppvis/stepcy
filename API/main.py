from flask import Flask,request,jsonify

# WARNING This needs to be removed in production

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app,support_credentials=True)

@app.route("/path-to")
@cross_origin()
def node_data():
    destination =request.args.get("from")
    start =request.args.get("start")
    return jsonify({"arb":"arb"})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
