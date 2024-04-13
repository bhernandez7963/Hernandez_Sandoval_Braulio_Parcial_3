from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nobre":"omar","enable":True},
    {"id":2, "nobre":"jessie","enable":False},
    {"id":3, "nobre":"jocelyn","enable":True},
    {"id":4, "nobre":"braulio","enable":False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
        return jsonify(tasks)

if __name__ == '__main__':
        app.run(debug=True)