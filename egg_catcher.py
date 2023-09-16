'''This script is a simple "Egg Catcher" game implemented using the tkinter GUI library. In the game, eggs of various colors fall from the top of the screen,
and the player's objective is to catch these eggs using a movable catcher at the bottom. The game tracks the player's score based on the number of eggs caught
and displays the remaining lives. The game's difficulty increases over time, with eggs falling at a faster rate. The player loses a life for every missed egg,
and the game ends when all lives are lost.
'''

from tkinter import Tk, Canvas, messagebox, font
import random

# Constants for the game settings
GAME_CONFIG = {
    'WIDTH': 800,
    'HEIGHT': 400,
    'EGG_WIDTH': 45,
    'EGG_HEIGHT': 55,
    'CATCHER_WIDTH': 100,
    'CATCHER_HEIGHT': 60,
    'CATCHER_COLOR': 'blue',
    'EGG_COLOR': ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'pink'],
    'MAX_EGGS': 5,
    'EGG_SPEED': 500,
    'EGG_INTERVAL': 4000,
    'DIFFICULTY_FACTOR': 0.95
}

# Global game variables
catcher = None
eggs = []
score = 0
lives_remaining = 3
missed = 0
canvas = None
score_display = None
lives_display = None

def create_catcher(canvas):
    """Create the catcher at the bottom center of the canvas."""
    x = GAME_CONFIG['WIDTH'] / 2 - GAME_CONFIG['CATCHER_WIDTH'] / 2
    y = GAME_CONFIG['HEIGHT'] - GAME_CONFIG['CATCHER_HEIGHT'] - 10
    catcher = canvas.create_arc(x, y, x + GAME_CONFIG['CATCHER_WIDTH'], y + GAME_CONFIG['CATCHER_HEIGHT'], start=200, extent=140, fill=GAME_CONFIG['CATCHER_COLOR'])
    return catcher

def initialize_game():
    """Initialize the game environment."""
    root = Tk()
    root.title('Egg Catcher')
    root.resizable(False, False)
    canvas = Canvas(root, width=GAME_CONFIG['WIDTH'], height=GAME_CONFIG['HEIGHT'], bg='deep sky blue')
    canvas.pack()
    fnt = font.nametofont('TkFixedFont')
    fnt.config(size=15)
    score_display = canvas.create_text(10, 10, anchor='nw', font=fnt, fill='darkblue', text=f'Score: {score}')
    lives_display = canvas.create_text(GAME_CONFIG['WIDTH'] - 10, 10, anchor='ne', font=fnt, fill='darkblue', text=f'Lives: {lives_remaining}')

    catcher = create_catcher(canvas)
    canvas.bind('<Left>', move_left)
    canvas.bind('<Right>', move_right)
    canvas.focus_set()

    egg_drop()
    root.after(100, catch_check)
    root.mainloop()

from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font

canvas_width = 800
canvas_height = 400

win = Tk()
c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'deep sky blue')
c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='sea green', width=0)
c.create_oval(-80,-80,120,120,fill='orange' , width=0)
c.pack()

color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)

score = 0
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='darkblue',text='Score : ' + str(score))

lives_remaning = 3
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='darkblue',text='Lives : ' + str(lives_remaning))

eggs = []

def create_eggs():
    x = randrange(10,740)
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        win.destroy()

def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    win.after(100,catch_check)

def increase_score(points):
    global score , egg_speed , egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text , text='Score : ' + str(score))

def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher,-20,0)

def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher,20,0)

c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)
c.focus_set()

win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop()
