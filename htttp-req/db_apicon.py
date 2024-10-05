from flask import Flask,render_template,request,jsonify
from flask_cors  import CORS, cross_origin


app = Flask(__name__)
CORS(app,support_credentials=True)

@app.route("/")
def hello_world():
     render_template('index.html')


@app.route("/get-path")
@cross_origin()
def node_data():
    start = request.args.get('start')
    to = request.args.get('to')
    print(start)
    print(to)
    return jsonify({"Hello":"world"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
