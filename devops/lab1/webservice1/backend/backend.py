from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return jsonify({'message': 'api1 is working'})


@app.route('/tasks', methods=['GET', 'POST'])
def tasks_route():
    if request.method == 'GET':
        return jsonify(tasks)
    elif request.method == 'POST':
        task = request.get_json()
        tasks.append(task)
        return jsonify({'message': 'Задача добавлена 1111'}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def task_route(task_id):
    if task_id >= len(tasks):
        return jsonify({'message': 'Задача не найдена 1111'}), 404
    if request.method == 'PUT':
        task = request.get_json()
        tasks[task_id] = task
        return jsonify({'message': 'Задача обновлена 1111'}), 200
    elif request.method == 'DELETE':
        del tasks[task_id]
        return jsonify({'message': 'Задача удалена 1111'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
