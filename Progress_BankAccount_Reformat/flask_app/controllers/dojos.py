from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojos

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos=Dojos.get_all()
    return render_template("dojos.html",all_dojos=dojos)

@app.route("/dojo/create", methods=["POST"])
def new_dojo():
    Dojos.save(request.form)
    return redirect("/dojos")

@app.route("/dojo/<int:id>")
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template("read(one)dojo.html", dojo=Dojos.get_one_with_ninjas(data))