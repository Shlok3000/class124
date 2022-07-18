from flask import Flask, jsonify, request 

app = Flask(__name__)

tasks = [
     {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Clean the dishes',
        'description': u'clean, rinse, dry, Put away',
        'done': False
    },
    {
        'id': 3,
        'title': u'Fall Guys',
        'description': u'minigames, races, survival, teams, logic, final',
        'done': False
    }
]

@app.route('/')
def Welcome():
    return("THese are my to do tasks/time passers")

@app.route('/add-Data',methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "messages":"Please provide the Data",
        },400)

    t = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json["title"],
        'description': request.json.get("description", ""),
        'done': False
    }
    tasks.append(t)
    return jsonify({
        'status': 'success',
        'message': 'task added successfully'
    })

@app.route('/get-data')
def getTask():
    return jsonify({
        "data":tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)