from flask import Flask, jsonify
import models
from db import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/most-cited-papers")
def most_cited_papers():
    with Session(engine) as session:
        statement = select(models.Papers).limit(1)
        results = session.exec(statement)
        print(results)
        return jsonify(results.first().dict)
