
from flask import Flask, request, redirect, send_from_directory
import json
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/style.css")
def style():
    return send_from_directory(BASE_DIR, "style.css")


@app.route("/tasks")
def get_tasks():
    return load_tasks()


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        tasks = load_tasks()
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
    return redirect("/")


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]
        save_tasks(tasks)
    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
#adding a command line

#testing PR review

#testing git fetch
