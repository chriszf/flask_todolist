from model import db, app, Task
import model

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    print tasks
    for task in tasks:
        return_str += "%s"%task + "<br>"

    return return_str

def go():
    app.run(debug=True)
