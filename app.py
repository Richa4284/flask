from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

## connecting to DB
def db_connection():
    conn = sqlite3.connect("users.sqlite")
    return conn

## get all users and add user
@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM user ")
        users = [
            dict(id=row[0], name=row[1], age=row[2], mobile=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            # return jsonify(users)
            return json.dumps(users)

    if request.method == "POST":
        new_name = request.form["name"]
        new_age = request.form["age"]
        new_mobile = request.form["mobile"]
        sql = """INSERT INTO user (name, age,  mobile)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_name, new_age, new_mobile))
        conn.commit()
        return f"user added successfully", 201


## GET USER DETAILS BY ID
@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE id=?", (id,))
    user = [
            dict(id=row[0], name=row[1], age=row[2], mobile=row[3])
            for row in cursor.fetchall()
        ]
    if user is not None:
        return json.dumps(user)


    

## GET USER BY AGE
@app.route("/user/age/<int:age>", methods= ["GET"])
def get_user_by_age(age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE age=?", (age,))
    
    users = [
            dict(id=row[0], name=row[1], age=row[2], mobile=row[3])
            for row in cursor.fetchall()
        ]
    if users is not None:
        return json.dumps(users)



## GET USER BY NAME
@app.route("/user/name/<name>", methods= ["GET"])
def get_user_by_name(name):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE name=?", (name,))
    users = [
            dict(id=row[0], name=row[1], age=row[2], mobile=row[3])
            for row in cursor.fetchall()
        ]
    if users is not None:
        return json.dumps(users)

## GET USER BY MOBILE NUMBER
@app.route("/user/mobile/<mobile>", methods= ["GET"])
def get_user_by_mobile(mobile):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE mobile=?", (mobile,))
    users = [
            dict(id=row[0], name=row[1], age=row[2], mobile=row[3])
            for row in cursor.fetchall()
        ]
    if users is not None:
        return json.dumps(users)






if __name__ == "__main__":
    app.run(debug=True)