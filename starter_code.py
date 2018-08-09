
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random 
turtle.up()
turtle.goto(0,400)
turtle.down()
turtle.write("SNAKE GAME >_<",move=False,align="center",font=("Arial",30))
turtle.up()
turtle.goto(0,0)
turtle.down()

food = turtle.clone()
turtle.register_shape("trash.gif")
food.shape("trash.gif")
food.pu()
food.hideturtle()
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1500
SIZE_Y=800
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 30
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
screen = turtle.Screen()
screen.setup(1600,900)
snake = turtle.clone()
snake.shape("square")
snake.color("green")
screen.bgpic("/home/student/siwarkhateb20_mini-proj/meet2018y1mini-proj/navyjack-bg.gif")


#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for t in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    snake_stamp1 = snake.stamp()
    stamp_list.append(snake_stamp1)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP


UP_EDGE = SIZE_Y/2
DOWN_EDGE = -(SIZE_Y/2)
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -(SIZE_X/2)



def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up #Update the snake drawing <- remember me later
    print("You pressed the up key!")

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up #Update the snake drawing <- remember me later
    print("You pressed the down key!")

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up#Update the snake drawing <- remember me later
    print("You pressed the right key!")

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up #Update the snake drawing <- remember me later
    print("You pressed the left key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up ,UP_ARROW)
turtle.onkeypress(down ,DOWN_ARROW)
turtle.onkeypress(right ,RIGHT_ARROW)
turtle.onkeypress(left ,LEFT_ARROW)
# Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+2
    max_x=int(SIZE_X/2/SQUARE_SIZE)-2
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-2
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+2
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    foodPos = (food_x,food_y)
    

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x,food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append(foodPos)
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    foodStamp = food.stamp()
    food_stamps.append(foodStamp)
    

make_food()
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
        




    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
   
    #piece of the tail
    
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]


    ##SNAK DY IF EATSELF
    if snake.pos() in pos_list[0:len(pos_list)-1]:
        print("game over")
        quit()



    
    ##SNAK DY IF EATSELF

    
    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()


    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])

        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        make_food()
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    if len(food_stamps) < 4:
        make_food()





        

    turtle.ontimer(move_snake,TIME_STEP)

move_snake()
