import random
import math
import simplegui


# helper function to start and restart the game

def start_game():
    global ran,tries
    ran=100
    tries=int(math.log(100,2))
    new_game(ran)
    
def new_game(ran):
    # initialize global variables used in your code here
    global secret_number
    secret_number=random.randrange(0,ran)
    #print('sn',secret_number)
    return secret_number

# define event handlers for control panel
def range100():
    global tries
    tries=math.log(100,2)
    new_game(100)

def range1000():
    global tries
    tries=math.log(1000,2)
    new_game(1000)
    
def input_guess(guess):
    # main game logic goes here	
    global tries
    tries -=1
    guess=int(guess)
    print('Guess was',guess)
    if guess>secret_number and tries>0:
        print('Lower')
        print('You have',tries, 'left')
    elif guess<secret_number and tries>0:
        print('Higher')
        print('You have',tries, 'tries left')
    elif guess==secret_number and tries>0:
        print('correct')
        start_game()
    elif tries==0:
        print('Game Over\n Answer was',secret_number)
        start_game()
    else:
        print('error')

    
# create frame

frame=simplegui.create_frame('Guess The Number',300,300)
frame.add_button('Run/Reset',start_game,100)
frame.add_input('Guess',input_guess,50)
frame.add_button('Range is [0,100)',range100,100)
frame.add_button('Range is [0,1000)',range1000,100)


