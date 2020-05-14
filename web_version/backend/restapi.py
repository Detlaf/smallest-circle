#!/usr/bin/env python3
from flask import Flask, request, jsonify
from worker import get_circle

app = Flask(__name__)
TASKS = {}

@app.route('/', methods=['GET'])
def list_tasks():
    tasks = {
        task_id: {
            'ready': task.ready()
        }
        for task_id, task in TASKS.items()
    }

    return jsonify(tasks) 

@app.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    response = {'task_id': task_id}
    task = TASKS[task_id]
    if task.ready():
        response['result'] = task.get()

    return jsonify(response)

@app.route('/', methods=['PUT'])
def put_task():
    task_id = len(TASKS)
    TASKS[task_id] = get_circle.delay()

    response = {
        'result': task_id
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()