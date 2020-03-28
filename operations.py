from flask import Flask, jsonify, request

app = Flask(__name__)

db = [
    {
        "student_id": ["1"],
        "first_name": ["Levi "],
        "last_name": ["Nair"],
        "dob(date of birth)": ["Oct 2"],
        "amount_due": ["Paid in full"]
    },
    {
        "student_id": ["2"],
        "first_name": ["ManSab"],
        "last_name": ["."],
        "dob(date of birth)": ["Dec 24"],
        "amount_due": ["negative 1 million"]
    },
    {
        "student_id": ["3"],
        "first_name": ["lucy"],
        "last_name": ["K"],
        "dob(date of birth)": ["May 7"],
        "amount_due": ["4000"]
    }
]

@app.route('/db')
def hello():
    print("Hello")
    return jsonify(db)

#ADD
@app.route('/db', methods=['POST'])
def add_db():
    student = request.get_json()
    db.append(student)
    return {'id': len(db)}, 200

#UDATE
@app.route('/db/<int:index>', methods=['PUT'])
def update_db(index):
    student = request.get_json()
    db[index] = student
    return jsonify(db[index]), 200

#DELETE
@app.route('/db/<int:index>', methods=['DELETE'])
def delete_db(index):
    db.pop(index)
    return 'None', 200

app.run()