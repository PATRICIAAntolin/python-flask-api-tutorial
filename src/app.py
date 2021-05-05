from flask import Flask
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": True },
    { "label": "My second task", "done": True }
]
json_text = flask.jsonify(todos)

@app.route('/todos', methods=['GET'])
def hello_world():
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)