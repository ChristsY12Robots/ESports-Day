#Collison example by Miles 25/11/17
#I am sure that this could be made much more efficient, so dont hesitate to change anything to make the program better
#Please feel free to fiddle with the numbers to test and check for errors, and remember this is an example so I've had to simulate the objects in the simplest way possible

#I came up with this idea this morning, its advantage is the fact that the main program can do it, and it only needs to get data from the objects once
#I am in no way saying this is the most effcient way of completing this task, but it is the best I can think of. It potentially only needs to search 2n times, n being the number of objects

#for this example make 2 VERY simple classes
import random

#robot class
class Robot():
    def __init__(self):
        self.xCoord = 0
        self.yCoord = 0
        self.name = "Robot"
        self.scrappile = False #this attraibute coudl be used in a first if statement to hinder movement, that way, the main program does not need to know what objects are dead

    def get_pos(self):
        #this stores the pos as a string for the convinence of this program, but this could be done elsewhere
        coords = (str(self.xCoord)+","+str(self.yCoord)) #this is only an example and could/can be adapted
        return(coords)

    def change_pos(self, x, y):
        self.xCoord = x
        self.yCoord = y

    #this changes the robots 'state'
    def change_state(self):
        self.name = "Scrappile"
        self.scrappile = True
        #scoreboard += 1 <-- For final scoreboard

#player class
class Player():
    def __init__(self):
        self.xCoord = 4
        self.yCoord = 6

    def get_pos(self):
        coords = (str(self.xCoord)+","+str(self.yCoord)) #see above
        return(coords)

    #although this object has no state to change, it is easier for the method to have the same name cross class
    def change_state(self):
        pass
        #I don't know what to say here
        #game_over = True??


# a little function to simulate something(?) which may already have been created in the full program
def example_creation():
    player = Player()
    object_list = []
    object_list.append(player)
    for instance_create in range(0, 50):
        robot = Robot()
        #these lines simulate many different robot positions
        x_create = random.randint(0,5)
        y_create = random.randint(0,5)
        #giving the instance these coords
        robot.change_pos(x_create, y_create)
        object_list.append(robot)
    return(object_list)

# a function just to display the collisions, not necessary at all
def example_print(delete_list, object_list):
    print("Total objects:")
    for y in object_list:
        print(y, ": ", y.get_pos())
    print("\n\n")
    print("And objects collided:")
    for x in delete_list:
        print(x, ": ", x.get_pos())

#simple kill function
def kill_object(delete_list):
    for x in delete_list:
        x.change_state()
    

#THIS is the main overall function   
def main():
    #define
    object_list = example_creation()
    collision_dict = {}
    reference_list = []
    #finding each object inside the storage list
    for instance in object_list:
        pos = instance.get_pos()
        #finding if a collision has occured/if two objects have the same pos
        if pos in collision_dict:
            collision_value = collision_dict[pos]
            #just in case there has ALREADY been a collision at this pos -- scrappile or 3/4 way collision
            if type(collision_value) == type(reference_list):
                collision_value.append(instance)
            #else turning the value into a list to add multiple keys
            else:
                value_list = []
                value_list.append(collision_value)
                value_list.append(instance)
            collision_dict[pos] = value_list
        #else it adds the instance to the dictionary so that can check for later collsions
        else:
            collision_dict[pos] = instance

    #finding the keys with multiple values
    delete_list = []
    for x in collision_dict:
        #if the value is a list, a collision has occured
        if type(collision_dict[x]) == type(reference_list):
            to_delete = collision_dict[x]
            #fianlly, adding all 'dead' objects to a list
            for y in to_delete:
                delete_list.append(y)
        else:
            pass
    #this is just used to display
    example_print(delete_list, object_list)
    #From here, you could have a quick function to 'kill' the objects (change their state to a scrappile in the case of the robot)
    kill_object(delete_list)
    
        
        
    
    

main()
    
