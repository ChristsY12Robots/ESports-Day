#Gameboard proof of concept 22/11/17 Miles Burne
import time

gameboard = []
max_x = 10
max_y = 10
#creating a loop for number of rows
for value in range(0, max_x):
    row = []
    #loop for number of columns
    for number in range(0, max_y):
        row.append(0)
    gameboard.append(row)

#proper display of a gameboard
for rows in gameboard:
    print(rows)

print("\n\n\n")

x, y = 0, 0
nil = False
secondValue = 0
#an example of how simple movement can be acheived
for secondValue in range(0, 10):
    gameboard[y][x] += 1
    #removing the previous tile to 'move' the object
    if secondValue > 0:
        gameboard[x-1][y-1] = 0
    #displaying the gameboard
    for rows in gameboard:
        print(rows)
    print("\n\n\n")
    time.sleep(1)
    #these lines are all that changes each iteration, they could be replaced proper x/y coords?
    x += 1
    y += 1



