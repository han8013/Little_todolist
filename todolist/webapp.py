from flask import redirect, url_for, render_template
from model import app, Task

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)


@app.route("/add", methods=["GET"])
def make_task():
    return "Create a page for users to input a new task"

@app.route("/add", methods=["POST"])
def save_task():
    return "Save a task"

