from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        task_text = request.form.get("task")
        due_date = request.form.get("due")
        if task_text:
            tasks.append({"text": task_text, "due": due_date, "done": False})
    return render_template("index.html", tasks=tasks)

@app.route("/toggle/<int:index>")
def toggle(index):
    tasks[index]["done"] = not tasks[index]["done"]
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks.pop(index)
    return redirect("/")

@app.route("/edit/<int:index>", methods=["POST"])
def edit(index):
    new_text = request.form.get("new_text")
    new_due = request.form.get("new_due")
    tasks[index]["text"] = new_text
    tasks[index]["due"] = new_due
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)