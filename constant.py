"""
Constants for the project.
"""
from random import randint
from blessed import Terminal

# Instance of Terminal to use in the project
terminal = Terminal()

BORDER = "⬜️"
SNAKE = "🟦"
FOOD1 = "🟩"
FOOD2 = "🟨"
FOOD3 = "🟧"
FOOD4 = "🟥"
FOOD5 = "🟫"
FOOD6 = "🟪"

# generate random food
FOOD_LIST = [FOOD1, FOOD2, FOOD3, FOOD4, FOOD5, FOOD6]
FOOD_RANDOM = FOOD_LIST[randint(0, 5)]
