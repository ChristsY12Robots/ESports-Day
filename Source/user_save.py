#User_Save Version 1 by Miles
#This version creates one file per user and saves their game data to it

#this is the library which allows the fetching of a username, i hope its installed on the school machines? (it was already on mine...)
import getpass
import datetime

#creating a user class
class User():
    #constructor
    def __init__(self):
        self.username = getpass.getuser()
        self.fileCreated = False

    def get_username(self):
        return(self.username)

    def check_username(self, checkUser):
        checkUser = checkUser.strip(" ")
        if checkUser == self.username:
            return(True)
        else:
            return(False)

    def create_file(self):
        f = open(str(self.username+".txt"), "a+") #opening in append mode IMPORTANT
        file = f.read() #this is really weird, if the file exists it still says there is NOTHING in it?
        print(file)
        time = str(datetime.datetime.now())
        if len(file)>0:
            f.write(("new session at "+str(time)))
            f.close()
        else:
            f.write((str(self.username)+" created "+str(time)+"\n"))
            f.close()
        self.fileCreated = True

    def append_file(self, game, score):
        if self.fileCreated == False:
            self.create_file()
        f = open(str(self.username+".txt"), "a+")
        time = str(datetime.datetime.now())
        f.write(str(game)+","+str(score)+","+time+"\n")
        file = f.read() #WHY WON'T IT READ!!??!!
        print(file)
        f.close()
        
        
        
        
        
        
#setting up a few test examples
user = User()

#testing username checking
print("Checking Usernames example") #spaces are stripped
usernames = ["MiloIsDaBest!!1  ","Milo","myUsername","kermit","Milo   ", "Mil0","milo",]
for x in usernames:
    if user.check_username(x) == True:
        print(x, "is your real username")
    else:
        print("Bugger off,",x,"is not a real username")



#testing game adding
import random
games = ["space_invaders", "pacman", "robots", "tetris", "Civ5", "half-life_2_PyEdition"]
for x in range(0,10):
    randomGame = random.randint(0,5)
    randomScore = random.randint(0,100)
    user.append_file(games[randomGame], randomScore)
    print("file written to "+str(x))









