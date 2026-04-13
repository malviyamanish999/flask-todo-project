from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db

@app.route('/submittodoitem', methods=['POST'])
def submit():
    data = request.json
    db.items.insert_one({
        "name": data['itemName'],
        "description": data['itemDescription']
    })
    return {"message": "Saved"}