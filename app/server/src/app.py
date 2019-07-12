
from flask import Flask, render_template, jsonify
from .tasks import add

app = Flask(
    __name__, static_folder="../../frontend/dist", template_folder="../../frontend"
)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/api/test")
def test():
    print("HI")
    rsp = add.delay(4, 4)
    res = rsp.get()
    print(f"Sending {res}")
    return jsonify({"hello": res})
