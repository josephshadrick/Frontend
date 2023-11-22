import requests
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
headers = {"Content-Type": "application/json"}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/employees")
def get_employees():
    return render_template("employees.html", employees=requests.get(
        #"https://joseph-api-4ro5n.ondigitalocean.app/employees"
        "http://localhost:8080/employees"
        ).json()["employees"])

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def find_record():
    name = request.form["user"]
    response = requests.post(
        #"https://joseph-api-4ro5n.ondigitalocean.app/login"
        "http://localhost:8080/login"
        ,headers=headers,json={"name": name,"pswd": request.form["pswd"]}
        ).text
    if response == "login success":
        return render_template("loginsuccess.html",name=name)
    return render_template("loginfailure.html")

@app.route("/employees", methods=["POST"])
def change_employees():
    if request.form["add"]:
        requests.post(
            #"https://joseph-api-4ro5n.ondigitalocean.app/employees"
            "http://localhost:8080/employees"
            ,headers=headers,json={"name": request.form["add"]})
    else:
        requests.delete(
            #"https://joseph-api-4ro5n.ondigitalocean.app/employees/"+request.form["text"]
            "http://localhost:8080/employees/"+request.form["delete"]
            )
    return get_employees()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)