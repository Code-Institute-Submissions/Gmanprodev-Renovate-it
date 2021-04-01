import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
print(os.environ.get("MONGO_URI"))

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_tips")
def get_tips():
    tips = list(mongo.db.tips.find())
    return render_template("tips.html", tips=tips)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("Signup Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>")
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    tips = list(mongo.db.tips.find({"username": session["user"]}))
    if session["user"]:
        return render_template("profile.html", username=username, tips=tips)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You are logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_tips", methods=["GET", "POST"])
def add_tips():
    if request.method == "POST":
        tip = {
            "category_name": request.form.get("category_name"),
            "username": session["user"],
            "location": request.form.get("location"),
            "tip": request.form.get("tip")
        }
        mongo.db.tips.insert_one(tip)
        flash("Tip Successfully Added")
        return redirect(url_for("get_tips"))

    categories = mongo.db.categories.find().sort("category_name, 1")
    return render_template("add_tips.html", categories=categories)


@app.route("/edit_tips/<tips_id>", methods=["GET", "POST"])
def edit_tips(tips_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "username": session["user"],
            "location": request.form.get("location"),
            "tip": request.form.get("tip")
        }
        mongo.db.tips.update({"_id": ObjectId(tips_id)}, submit)
        flash("Tip Updated!")

    tip = mongo.db.tips.find_one({"_id": ObjectId(tips_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_tips.html", tips=tip, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
