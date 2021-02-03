from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/play/<int:number>/<color>")
def playbox(number, color):
    return render_template("index.html", num= 35, color= color)

if __name__=="__main__":
    app.run(debug=True)
