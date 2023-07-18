"""
Constants for the project.
"""
from random import randint
from blessed import Terminal

# Instance of Terminal to use in the project
term = Terminal()

BORDER = "⬜️"
SNAKE = "🟦"
FOOD1 = "🟩"
FOOD2 = "🟨"
FOOD3 = "🟧"
FOOD5 = "🟫"
FOOD6 = "🟪"
FOOD4 = "🟦"
SPACE = "　"
APPLE = "🍎"
BANANA = "🍌"
CHERRY = "🍒"
GRAPES = "🍇"
LEMON = "🍋"
ORANGE = "🍊"
PEACH = "🍑"
PEAR = "🍐"
WATERMELON = "🍉"
FRUITS_LIST = [APPLE, BANANA, CHERRY, GRAPES, LEMON, ORANGE, PEACH, PEAR, WATERMELON]

UP = term.KEY_UP
RIGHT = term.KEY_RIGHT
LEFT = term.KEY_LEFT
DOWN = term.KEY_DOWN
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]
MOVEMENT_MAP = {LEFT: [0, -1], UP: [-1, 0], RIGHT: [0, 1], DOWN: [1, 0]}
WASD_MAP = {'w': UP, 'a': LEFT, 's': DOWN, 'd': RIGHT, 'W': UP, 'A': LEFT, 'S': DOWN, 'D': RIGHT}
dead = False

# -------CONFIG--------
BORDER = '⬜️'
BODY = '🟩'
HEAD = '🟥'
SPACE = '　'
APPLE = '🍎'
