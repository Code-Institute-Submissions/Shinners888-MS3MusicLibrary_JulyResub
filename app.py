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


mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    works = mongo.db.works.find()
    return render_template("home.html", works=works)


@app.route("/browse")
def browse():
    works = mongo.db.works.find()
    return render_template("browse.html", works=works)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_already_exists = mongo.db.site_users.find_one(
            {"username": request.form.get("username").lower()})

        if user_already_exists:
            flash("Oops, looks like someone already picked that username! Try again :)")
            return redirect(url_for("register"))

        register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
        mongo.db.site_users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("mymusic", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_already_exists = mongo.db.site_users.find_one(
            {"username": request.form.get("username").lower()})

        if user_already_exists:
            if check_password_hash(
                user_already_exists["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "mymusic", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/mymusic/<username>", methods=["GET", "POST"])
def mymusic(username):
    username = mongo.db.site_users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("mymusic.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_work", methods=["GET", "POST"])
def add_work():
    if request.method == "POST":
        work = {
            "genre": request.form.get("genres.genre_name"),
            "composer": request.form.get("composer"),
            "work": request.form.get("work"),
            "description": request.form.get("description"),
            "url": request.form.get("url"),
            "user_added": session["user"]
        }
        mongo.db.works.insert_one(work)
        flash("Thank You For Contributing!!")
        return redirect(url_for("browse"))
    genres = mongo.db.genres.find().sort("genre_id", 1)
    return render_template("add_work.html", genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
