import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    """
    Gets the books from the server and
    displays them on the site.
    """
    genre = list(mongo.db.genres.find())
    book = list(mongo.db.books2.find())
    return render_template("books.html", books2=book, genres=genre)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Allows users to create an account, and post
    the details to the server.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))
        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "birthday": request.form.get("birthday")
        }
        mongo.db.users.insert_one(signup)
        session["user"] = request.form.get("username").lower()
        flash("You've signed up!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Existing users to login to thir account.
    """
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
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/reviews")
def reviews():
    """
    Gets and displays the reviews stored on the
    server and shows them on the site.
    """
    review = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=review)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    Allows users to add a review to the site and
    stores it on the server.
    """
    if request.method == "POST":
        review = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_description": request.form.get("book_description"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added")
        return redirect(url_for("reviews"))

    genres = mongo.db.genres2.find().sort("genre_name", 1)
    return render_template("add_review.html", genres2=genres)


@app.route("/edit_review/<reviews_id>", methods=["GET", "POST"])
def edit_review(reviews_id):
    """
    Lets users edit their reviews.
    """
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_description": request.form.get("book_description"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(reviews_id)}, submit)
        flash("Review successfully updated")
        return redirect(url_for("reviews"))
    review = mongo.db.reviews.find_one({"_id": ObjectId(reviews_id)})
    genres = mongo.db.genres2.find().sort("genre_name", 1)
    return render_template("edit_review.html", reviews=review, genres2=genres)


@app.route("/contact_page", methods=["GET", "POST"])
def contact_page():
    """
    Enables the form on contact page to be submitted
    to the server.
    """
    if request.method == "POST":
        improvement = {
            "email": request.form.get("email").lower(),
            "feedback": request.form.get("feedback").lower()
        }
        mongo.db.improvements.insert_one(improvement)
        flash("Thank you for your feedback")
    return render_template('contact_page.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
