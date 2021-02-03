from flask import Flask
app = Flask(__name__)

@app.route("/") #our root route represents localhost:5000
def home():
	return "Hello World!"
@app.route("/dojo")
def games():
    return "Hello Dojo!!"

@app.route("/players/<name>") #routing with parameters
def showPlayerInfo(name):
    return f"hello!: {name} "

@app.route("/teams/<teamName>/<int:numchampionships>")
def teamChamps(teamName, numchampionships):
    print("*"*20)
    print(teamName)
    print(numchampionships)
    print("*"*20)

    return f"{teamName} won!" * numchampionships






if __name__=="__main__":
	app.run(debug=True)