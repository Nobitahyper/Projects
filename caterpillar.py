'''This script implements a simple game where a caterpillar moves around the screen, trying to consume leaves.
The game uses the turtle module for graphics and animation. As the caterpillar eats leaves, it grows in length,
and the player's score increases. The game becomes more challenging as the caterpillar's speed increases with
its length. The game ends if the caterpillar moves outside the screen boundary.
'''

import turtle as t
import random as rd

# Constants for the game and mechanics
INITIAL_CATERPILLAR_SPEED = 2
INITIAL_CATERPILLAR_LENGTH = 3
SCORE_INCREMENT = 10
LEAF_DISTANCE_THRESHOLD = 20
WINDOW_WIDTH_BOUNDARY = 200
WINDOW_HEIGHT_BOUNDARY = 200
LEVEL_THRESHOLD = 100
BOUNDARY_MARGIN = 10

def initialize_game():
    "Initialize the game environment."
    t.bgcolor('yellow')

    # Caterpillar configuration
    caterpillar.speed(0)
    caterpillar.shape('square')
    caterpillar.penup()
    caterpillar.hideturtle()

    # Leaf configuration
    leaf_shape = ((0, 0), (14, 5), (18, 9), (20, 20), (9, 18), (5, 14))
    t.register_shape('leaf', leaf_shape)
    leaf.shape('leaf')
    leaf.color('green')
    leaf.penup()
    leaf.hideturtle()
    leaf.speed()

    # Display starting message
    text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))

def check_outside_window(x, y):
    "Check if the caterpillar is outside the game window."
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside

def check_outside_boundary(x, y):
    "Check if the caterpillar is outside the game boundary."
    left_wall = -WINDOW_WIDTH_BOUNDARY + BOUNDARY_MARGIN
    right_wall = WINDOW_WIDTH_BOUNDARY - BOUNDARY_MARGIN
    top_wall = WINDOW_HEIGHT_BOUNDARY - BOUNDARY_MARGIN
    bottom_wall = -WINDOW_HEIGHT_BOUNDARY + BOUNDARY_MARGIN
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside

def update_game_over():
    "End the game and display the 'GAME OVER' message."
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Aerial', 30, 'normal'))

def update_score_display(score):
    "Update and display the current score."
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(score), align='right', font=('Arial', 40, 'bold'))

def place_new_leaf():
    "Place a new leaf in a random position within the game window."
    leaf.hideturtle()
    leaf.setx(rd.randint(-WINDOW_WIDTH_BOUNDARY + BOUNDARY_MARGIN + 10, WINDOW_WIDTH_BOUNDARY - BOUNDARY_MARGIN - 10))
    leaf.sety(rd.randint(-WINDOW_HEIGHT_BOUNDARY + BOUNDARY_MARGIN + 10, WINDOW_HEIGHT_BOUNDARY - BOUNDARY_MARGIN - 10))
    leaf.showturtle()

def draw_boundary():
    "Draw a visible boundary for the game window."
    boundary_drawer = t.Turtle()
    boundary_drawer.penup()
    boundary_drawer.color('red')
    boundary_drawer.goto(-WINDOW_WIDTH_BOUNDARY + BOUNDARY_MARGIN, WINDOW_HEIGHT_BOUNDARY - BOUNDARY_MARGIN)
    boundary_drawer.pendown()
    for _ in range(2):
        boundary_drawer.forward(2 * (WINDOW_WIDTH_BOUNDARY - BOUNDARY_MARGIN))
        boundary_drawer.right(90)
        boundary_drawer.forward(2 * (WINDOW_HEIGHT_BOUNDARY - BOUNDARY_MARGIN))
        boundary_drawer.right(90)
    boundary_drawer.hideturtle()

def move_leaf_based_on_level(score):
    "Move the leaf slightly based on the current level."
    level = score // LEVEL_THRESHOLD
    leaf.setx(leaf.xcor() + rd.randint(-level, level))
    leaf.sety(leaf.ycor() + rd.randint(-level, level))

def game_loop():
    "Main game loop."
    draw_boundary()
    score = 0
    caterpillar_speed = INITIAL_CATERPILLAR_SPEED
    caterpillar_length = INITIAL_CATERPILLAR_LENGTH
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    update_score_display(score)
    place_new_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < LEAF_DISTANCE_THRESHOLD:
            place_new_leaf()
            move_leaf_based_on_level(score)
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 0.2
            score += SCORE_INCREMENT
            update_score_display(score)
        x, y = caterpillar.pos()
        if check_outside_boundary(x, y):
            update_game_over()
            break

def move(direction):
    "Change the caterpillar's direction based on user input."
    if direction == 'up':
        if caterpillar.heading() == 0 or caterpillar.heading() == 180:
            caterpillar.setheading(90)
    elif direction == 'down':
        if caterpillar.heading() == 0 or caterpillar.heading() == 180:
            caterpillar.setheading(270)
    elif direction == 'left':
        if caterpillar.heading() == 90 or caterpillar.heading() == 270:
            caterpillar.setheading(180)
    elif direction == 'right':
        if caterpillar.heading() == 90 or caterpillar.heading() == 270:
            caterpillar.setheading(0)

def start():
    "Start the game."
    global game_started
    if game_started:
        return
    game_started = True
    text_turtle.clear()
    game_loop()

def restart_game(x, y):
    "Restart the game when the 'R' key is pressed."
    global game_started
    if not game_started:
        t.clear()
        initialize_game()
        game_started = False
        text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))

# Setup game environment
caterpillar = t.Turtle()
leaf = t.Turtle()
game_started = False
text_turtle = t.Turtle()
text_turtle.hideturtle()
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

initialize_game()

# Key bindings
t.onkey(lambda: start(), 'space')
t.onkey(lambda: move('up'), 'Up')
t.onkey(lambda: move('right'), 'Right')
t.onkey(lambda: move('down'), 'Down')
t.onkey(lambda: move('left'), 'Left')
t.onkey(lambda: restart_game(), 'R')
t.listen()
t.mainloop()
