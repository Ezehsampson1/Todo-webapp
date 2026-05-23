from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


todos = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        task = request.form["todo"].strip()

        if task:
            todos.append(task)


        return redirect(url_for("index"))

    return render_template("index.html", todos=todos)



@app.route("/delete/<int:index>")
def delete(index):
    
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)