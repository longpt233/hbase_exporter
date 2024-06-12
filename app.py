from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/jmx', methods=['GET','POST'])
def echo():
    data = {"beans":[]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)