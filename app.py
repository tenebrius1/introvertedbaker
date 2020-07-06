from flask import Flask, render_template, redirect

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/ccc")
def ccc():
    return render_template("ccc.html")

@app.route("/biscotti")
def biscotti():
    return render_template("biscotti.html")

@app.route("/hummingbird")
def hummingbird():
    return render_template("hummingbird.html")

@app.route("/lemon_cake")
def lemon_cake():
    return render_template("lemon_cake.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/about")
def about():
    return render_template("about.html")