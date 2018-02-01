#35 Save by Miles Burne 1/2/18

import getpass
import os
#import profile

#function to recieve the file on the other end, needs an input of the game name ("pacman","tetris")
def reciever(game):
    username = (getpass.getuser()).lower() #I found an issue where if the user logs in with caps enabled, the username will be all caps in program. Not a big deal but may as well solve it.
    '''user_profile = profile.User_Profile(username) #getting user profile'''
    filename = (str(username)+"_"+str(game)+".esp") #getting filename
    f = open(filename, "r")
    content = f.read()
    f.close()
    content = content.split("\n") #file now split into number of records
    for x in content:
        x = x.split(",") #now split into [score, game]
        '''
        user_profile.update_score(x[0])# updating the score
        user_profile.add_game_record(game)
        user_profile.save()
        '''
    os.remove("filename") #not sure about this, could be used for cheat prevention ie lower the window of time the user would have to find and change the file? (This deletes the file)    
        
#to be called as:    
reciever("pacman")
reciever("tetris")
