import random
import copy
from collections import deque
from blessed import Terminal
from constant import *

term = Terminal()

def random_fruit(FRUITS_LIST):
  return random.choice(FRUITS_LIST)


direction = RIGHT


# initial snake position
snake = deque([[6, 5], [6, 4], [6, 3]])
# initial food position
food = [5, 10]
h, w = 10, 15 # height, width
score = 0
# initial speed
speed = 3
# max speed
MAX_SPEED = 6
# -----CONFIG END------

def list_empty_spaces(world, space):
  result = []
  for i in range(len(world)):
    for j in range(len(world[i])):
      if world[i][j] == space:
        result.append([i, j])
  return result
# start taking input from the keyboard and hide other cursor
with term.cbreak(), term.hidden_cursor():
  # clear the screen
  print(term.home + term.clear)
  
  # Initialize the world
  world = [[SPACE] * w for _ in range(h)]
  for i in range(h):
    world[i][0] = BORDER
    world[i][-1] = BORDER
  for j in range(w):
    world[0][j] = BORDER
    world[-1][j] = BORDER
  for s in snake:
    world[s[0]][s[1]] = BODY
    head = snake[0]
  world[head[0]][head[1]] = HEAD

  fruit = random_fruit(FRUITS_LIST)
  print(fruit)

  world[food[0]][food[1]] = fruit
  for row in world:
    print(' '.join(row))
  print('use arrow keys to move!')
  print('I recommend expanding the terminal window')
  print('so the game has enough space to run')

  val = ''
  moving = False

  while val.lower() != 'q':
    val = term.inkey(timeout=1/speed)
    if val.code in [UP, RIGHT, DOWN]:
      moving = True
    if not moving:
      continue

    if val.code == UP and direction != DOWN:
      direction = UP
    elif val.code == RIGHT and direction != LEFT:
      direction = RIGHT
    elif val.code == DOWN and direction != UP:
      direction = DOWN
    elif val.code == LEFT and direction != RIGHT:
      direction = LEFT
    
    head = copy.copy(snake[0])
    if direction == UP:
      head[0] -= 1
    elif direction == RIGHT:
      head[1] += 1
    elif direction == DOWN:
      head[0] += 1
    elif direction == LEFT:
      head[1] -= 1
    
    heading = world[head[0]][head[1]]
    ate_food = False
    if heading == fruit:
      ate_food = True
      empty_spaces = list_empty_spaces(world, SPACE)
      food = random.choice(empty_spaces)
      fruit = random_fruit(FRUITS_LIST)
      world[food[0]][food[1]] = fruit
      speed = min(MAX_SPEED, speed * 1.07)
    elif heading == BORDER:
      break
    elif heading == BODY and head != snake[-1]:
      break

    if not ate_food:
      tail = snake.pop()
      world[tail[0]][tail[1]] = SPACE
    world[head[0]][head[1]] = HEAD
    snake.appendleft(head)

    print(term.move_yx(0, 0))
    for row in world:
      print(' '.join(row))
    
    score = len(snake) - 3
    print(f'score: {score} - speed: {speed:.1f}   ')
    print(term.clear_eos, end='')

print('game over!')