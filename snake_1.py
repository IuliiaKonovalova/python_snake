import curses
from random import randint


curses.initscr()
# y comes first, then x
win = curses.newwin(20, 60, 0, 0)
# key pad mode to get special keys like arrow keys
win.keypad(1)
# do not echo keys on the screen
curses.noecho()

# hide cursor
curses.curs_set(0)
# draw border
win.border(0)
# do not wait for user input, getch() returns -1 if no key is pressed
win.nodelay(1)


# snake and food
# set up coordinates for snake
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)
# draw food
win.addch(food[0], food[1], '*')
# define keys
ESC = 27
key = curses.KEY_RIGHT

# main logic
score = 0
while key != ESC:
    # show score
    win.addnstr(0, 2, 'Score: ' + str(score) + ' ', 20)
    # set up snake speed
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)
    # get previous key
    prev_key = key

    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    
    # insert new head
    snake.insert(0, (y, x))

    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # if snake runs over itself
    if snake[0] in snake[1:]: break
    # if snake hit the food
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '*')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    # for coord in snake:
    #     win.addch(coord[0], coord[1], '#')

    # win.addch(food[0], food[1], '*')
    win.addch(snake[0][0], snake[0][1], '#')
curses.endwin()

print("Game Over")
print(f"Final Score = {score}")