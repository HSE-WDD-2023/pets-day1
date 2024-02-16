from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/success", methods=["POST"])
def success():
    # get the info the user filled out on the form
    owner = request.form.get("owner")
    pet = request.form.get("pet")
    # load the success page
    return render_template("success.html",
                           owner_name=owner,
                           pet_name=pet)
