from flask import Flask, render_template, request
import smtplib
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
    message="You have registered"
    if not name or not gender:
        return "<h1>Enter name or gender</h1>" 
    student.append({"id":len(student)+1,"name":name,"gender":gender})
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("ajayrathnam16703@gmail.com","ympwopoycysovmzk")
    server.sendmail("ajayrathnam16703+python@gmail.com",email,message)
    print(student)
    return f"<h1>{name} registered</h1>"