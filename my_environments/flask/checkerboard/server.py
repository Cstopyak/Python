from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("checker.html")

@app.route("/bigger")
def box():
    return render_template("biggerchecker.html")

@app.route("/giant")
def box2():
    return render_template("giantchecker.html")

if __name__=="__main__":
    app.run(debug=True)
