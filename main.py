from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key="praveen"
app.permanent_session_lifetime=timedelta(seconds=10)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("userpage"))
    else:
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("userpage"))
        else:
            #return redirect(url_for("user",name=user))
            return render_template("login.html")

# @app.route("/<name>")
# def user(name)
    # return render_template("user.html",name=name)

@app.route("/userpage")
def userpage():
    if "user" in session:
        user=session["user"]
        print(session)
        return render_template("user.html",name=user)
    else:
        flash("You not logged your name")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user",None)
        flash("You have logged out!") 
        print(session)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)