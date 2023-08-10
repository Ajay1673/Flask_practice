from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


student = []
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')
@app.route("/registerform",methods=["POST"])
def registerform():
    name=request.form.get("name")
    email=request.form.get("email")
    gender=request.form.get("gender")
    if not name or not email or not gender:
        return "Error"
    with open("registration.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow((name,email,gender))
    print(student)
    return redirect("/")

@app.get("/registered")
def registered():
    with open("registration.csv","r") as file:
        reader=csv.reader(file)
        students=list(reader)
        print(students)
    return render_template("registered.html",students=students)
