import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a flask app"

@app.route("/employees")
def get_employees():
    data = requests.get("https://joseph-api-4ro5n.ondigitalocean.app/employees").json()
    return render_template('employees.html', employees=data["employees"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)