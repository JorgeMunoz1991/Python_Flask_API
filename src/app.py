from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}),

# Estas dos líneas siempre deben estar al final de tu archivo app.py.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
