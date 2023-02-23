from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)


# Create route decorator
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    first_name = "Matthew"
    stuff = "This is <strong>Bold</strong> Text"
    favourite_pizza = ["Pepperoni", "Cheese", "Mushroom", "Donor Kebab"]
    return render_template("user.html", username=name, first_name=first_name, stuff=stuff,
                           favourite_pizza=favourite_pizza)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
