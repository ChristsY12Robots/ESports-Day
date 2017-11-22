#pathfinding 22/11/17 Miles
#in development
'''
Attempt at creating a method to find a robots move based on the players postion, to be used as a method in the robot class

Note:
- this relies on the fact that 0,0 is the top left on the grid, though this can be changed

'''

#method to find the direction in which the robot should move, for use in robot class

'''
As these classes haven't been created yet, please accept substitute
Let RobotX = self.xCoord
Let RobotY = self.yCoord
Let PlayerX = player.xCoord
Let playerY = player.yCoord
'''

#method needs the players X,Y and returns the robots new X,Y
#method could perhaps be passed just the object(player) but is this bad practice?
def find_move(RobotX, RobotY, PlayerX, PlayerY): #normally: self, player.xCoord, player.yCoord
    newX, newY = RobotX, RobotY #initializing the variables that will need to be returned, essentially the coords after the move
    #multiple IF statements seems crude but its the best I could come up  with without over complicating (could have used dictionarys but it's not necessary)
    if PlayerX > RobotX:
        newX += 1
    if PlayerX < RobotX:
        newX -= 1
    if PlayerY > RobotY:
        newY += 1
    if PlayerY < RobotY:
        newY -= 1
    return(newX, newY)

x, y = (find_move(1,2,3,2))
print("("+str(x)+","+str(y)+")")
