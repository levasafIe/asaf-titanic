from flask import Flask, request

from titanic_utils.str_utils import extract_titles

app = Flask(__name__)


@app.route("/")
def hello():
    # name = request.args["name"]  # Too strict, fails if ?name= is not passed
    # if "name" in request.args
    print("Parameters: ", request.args)
    name = request.args.get("name")
    greeting = request.args.get("greeting", "Hello")
    if name is not None:
        return f"{greeting}, {name}!"
    else:
        return "Hello, stranger"


@app.route("/extract_titles")
def extract_titles_endpoint():
    return extract_titles(request.args["name"])
