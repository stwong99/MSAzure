from fastapi import FastAPI
import uvicorn

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return "Hello, World!"


#try flask method
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

