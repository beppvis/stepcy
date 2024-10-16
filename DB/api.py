import node_db
import backend2
from flask import Flask,render_template,request,jsonify
from flask_cors  import CORS, cross_origin




app = Flask(__name__)
CORS(app,support_credentials=True)

@app.route("/")
def hello_world():
    return "<p>Hello world :)</p>"


@app.route("/path-to")
@cross_origin()
def node_data():
    start = request.args.get('start')
    to = request.args.get('to')
    out= {}
    out["path"] = backend2.get_shortest_path(start,to)
    print("Shortes path is : ",out["path"])
    
    return jsonify(out)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
