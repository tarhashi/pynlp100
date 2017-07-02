# coding: utf-8
from flask import Flask, request, jsonify
from mongo_db import MongoDb

mongoDb = MongoDb()
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, Flask!"

@app.route("/")
def search():
    name = request.args.get('name')
    tag = request.args.get('tag')
    condition = {}
    if name:
        condition['$or'] = [{'name':name}, {'aliases.name':name}]
    if tag:
        condition['tags.value'] = tag
    print(condition)
    results = mongoDb.find('artists', condition, 'rating.count', 10)
    resultSet = []
    for result in results:
        result.pop('_id')
        resultSet.append(result)
    return jsonify(resultSet)

if __name__ == "__main__":
    app.run()