
def startGame():
    print ("------------------------------------------------")
    print "Welcome to my Home."
    print ("------------------------------------------------")
    print  "To move around, use E, W, N, S"
    print ("------------------------------------------------")
    

def showRoom():
    print ("--------------------------------------------------")
    print ("You walked in to the " + house[currentRoom]["name"])
    print ("--------------------------------------------------")
    

house = {
    1: {"name" :"Kitchen", "N" : 7},
    2: {"name" : "Hallway", "S" : 4, "N" : 5, "E" : 1, "W" : 7 },
    3: {"name" : "Bathroom", "N" : 7, "W" : 5},
    4: {"name" : "Garden", "W" : 5},
    5: {"name" : "Master bedroom","S" : 3, "E" : 4, "W" : 6},
    6: {"name" : "Library", "W" : 7, "E": 5},
    7: {"name" : "Living room", "S": 1, "E" : 6},
    }

currentRoom = 2
startGame()
showRoom()

while True:
    newMove = raw_input("Explore my House: ").upper()
    if newMove in house[currentRoom]:
        currentRoom = house[currentRoom][newMove]
        showRoom()
              
    else:        
        print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print "That's a wall"
        print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        showRoom()
