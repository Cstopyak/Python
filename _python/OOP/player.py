class Player:
    def __init__(self, nameInput, ageInput):
        #attributes
        self.points = 0
        self.name = nameInput
        self.age = ageInput 

    #methods
    def scorePoints(self, numPoints):
        self.points += numPoints
        return self

    def losePoints(self, numPoints):
        self.points -= numPoints
        return self

    def displayStats(self):
        print(f"Player name: {self.name}. Points: {self.points}. Age: {self.age}")
        return self




p1 = Player("Lebron", 36)
p2 = Player("Kobe", 40)
p3 = Player("Iverson", 40)

print(f"player 1 points {p1.points}")
print(f"player 2 points {p2.points}")

#self is whatever object is calling the method
# p1.scorePoints(20)
# p1.losePoints(2)
# p1.scorePoints(10)
# p1.scorePoints(5)

p1.scorePoints(20).losePoints(2).scorePoints(10).scorePoints(5).displayStats()

p2.scorePoints(81).displayStats()
