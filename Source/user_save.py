#User_Save Version 1 by Miles

#if anyone can help, this is broken and i dont know why... 
#when trying to check if the file i have created exists i use:
#file = f.read()
#if len(file) > 0: ... but apparently no matter what 'file' is empty??
#this can be seen below



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

    def read_file(self, indicate):
        f = open(str(self.username+".txt"), "r")
        file = f.read()
        f.close()
        if indicate == 1:
            if len(file) > 1:
                return(True)
            else:
                return(False)
        else:
            output = []
            file = file.split("\n")
            for x in file:
                carry = x.split(",")
                if file[0] == x:
                    pass
                else:
                    output.append(carry)
            return(output)

    def create_file(self):
        f = open(str(self.username+".txt"), "a+") #opening in append mode IMPORTANT
        time = str(datetime.datetime.now())
        if self.read_file(1) == True:
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
        f.close()
        
        
        
        
        
        
#setting up a few test examples
user = User()

#testing username checking
print("Checking Usernames example") #spaces are stripped
usernames = ["MiloIsDaBest!!1  ","Milo","myUsername","kermit","Milo   ", "Mil0","milo","burnm035.318"]
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

#reading the file

file = user.read_file(0)
for x in range(0, len(file)-1):
    game = file[x][0]
    score = file[x][1]
    print(user.get_username()+" played "+game+" and got "+score)
        








