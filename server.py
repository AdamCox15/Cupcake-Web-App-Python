from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary


@app.route("/")
def home ():
    return render_template("index.html", cupcakes = get_cupcakes("newCupcakeList.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route("/cupcake_individual/<name>")
def individual_cupcake(name):
    return render_template("individual-cupcakes.html", cupcake = find_cupcake("newCupcakeList.csv",name))

@app.route("/order")
def order():
    return render_template("order.html", cupcakes = get_cupcakes("order.csv"))



@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("newCupcakeList.csv", name)

    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for("all_cupcakes"))
    else:
        return "Sorry cupcake not found."


if __name__ =="__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")