'''This script simulates the rolling of a dice. When executed, the program prompts the user to roll the dice, and upon confirmation,
it randomly selects a number between 1 and 6 (inclusive). The corresponding face of the dice, represented using ASCII art, is
then displayed. The user can continue rolling the dice as many times as desired.
'''

import random

def display_dice_face(number):
    """Display the face of the dice based on the provided number."""
    dice_faces = {
        1: [
            "----------",
            "|        |",
            "|    O   |",
            "|        |",
            "----------"
        ],
        2: [
            "----------",
            "|        |",
            "| O    O |",
            "|        |",
            "----------"
        ],
        3: [
            "----------",
            "|    O   |",
            "|    O   |",
            "|    O   |",
            "----------"
        ],
        4: [
            "----------",
            "| O    O |",
            "|        |",
            "| O    O |",
            "----------"
        ],
        5: [
            "----------",
            "| O    O |",
            "|    O   |",
            "| O    O |",
            "----------"
        ],
        6: [
            "----------",
            "| O    O |",
            "| O    O |",
            "| O    O |",
            "----------"
        ]
    }
    for line in dice_faces[number]:
        print(line)

def dice_simulator():
    """Dice simulator function."""
    print("Welcome to the dice simulator!")
    while True:
        number = random.randint(1, 6)
        display_dice_face(number)
        user_input = input("Do you want to roll the dice again? (y/n)").lower()
        if user_input != 'y':
            break

dice_simulator()
