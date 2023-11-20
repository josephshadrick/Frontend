import requests
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
headers = {"Content-Type": "application/json"}

@app.route("/")
def home():
    return "This is a flask app"

@app.route("/employees")
def get_employees():
    return render_template('employees.html', employees=requests.get(
        #"https://joseph-api-4ro5n.ondigitalocean.app/employees"
        "http://localhost:8080/employees"
        ).json()["employees"])

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