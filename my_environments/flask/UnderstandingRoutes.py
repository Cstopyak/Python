from flask import Flask
app = Flask(__name__)

@app.route("/") #our root route represents localhost:5000
def home():
    return "Hello This is the bootleg nba.com home page"

@app.route("/games")
def games():
    return "Games!!"

@app.route("/players/<pname>") #routing with parameters
def showPlayerInfo(pname):
    return f"Place holder to show info about one player: {pname} "

@app.route("/teams/<teamName>/<int:numchampionships>")
def teamChamps(teamName, numchampionships):
    print("*"*20)
    print(teamName)
    print(numchampionships)
    print("*"*20)

    return f"{teamName} won!" * numchampionships




if __name__=="__main__":
    app.run(debug=True)