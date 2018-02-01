#Python 2.7 Save Function

#Done out of function
import getpass


#fuction to save
def save_file(score):
    game = "pacman" #could be changed
    file_name = str(str(getpass.getuser().lower())+"_"+game+".esp")
    f = open(file_name, "a")
    f.write(str(score)+","+game)
    f.close()

def file_game_start():
    game = "pacman"
    file_name = str(str(getpass.getuser().lower())+"_"+game+".esp")
    f = open(file_name, "w")
    f.close()
    
file_game_start()
save_file(15)
