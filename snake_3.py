import curses
from random import randint



def calculate_next_coordinates(key, snake, x, y, direction, win):
    """
    Calculate next coordinates, update snake, update direction if necessary
    Args:
        key: key pressed by user
        snake: list of tuples, coordinates of snake
        x: x coordinate of snake head
        y: y coordinate of snake head
    """
    
    # calculate next coordinates
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
    if y == 0 or y == 19 or x == 0 or x == 59:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
        # if so, update direction:
        if y == 0:
            y = 18
        elif y == 19:
            y = 1
        elif x == 0:
            x = 58
        elif x == 59:
            x = 1
        # update direction
        if direction == curses.KEY_DOWN:
            direction = curses.KEY_UP
        elif direction == curses.KEY_UP:
            direction = curses.KEY_DOWN
        elif direction == curses.KEY_LEFT:
            direction = curses.KEY_RIGHT
        elif direction == curses.KEY_RIGHT:
            direction = curses.KEY_LEFT
        # update position
        snake.insert(0, (y, x))

def game_over(score):
    """
    Game over logic
    Args:
        score: score of the game
    """
    curses.endwin()

    print("Game Over")
    print(f"Final Score = {score}")

def main():
    """
    Main function to run the game
    1. set up the screen
    2. set up the snake
    3. set up the food
    4. set up the game logic
    5. set up the game over logic
    6. control the score
    """
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
    snake = [(4, 10), (4, 9), (4, 8)]
    food = (10, 20)
    # draw food
    win.addch(food[0], food[1], '*')

    ESC = 27
    key = curses.KEY_RIGHT
    # set up direction of 
    direction = curses.KEY_RIGHT
    score = 0
    lives = 3


    # main logic
    while key != ESC and lives > 0:
        # show score
        win.addnstr(0, 2, 'Score: ' + str(score) + ' ', 20)
        win.addnstr(0, 20, 'Lives: ' + str(lives) + ' ', 20)
        # set up snake speed
        win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)
        # get previous key
        prev_key = key

        event = win.getch()
        key = event if event != -1 else prev_key

        if key not in [
            curses.KEY_LEFT,
            curses.KEY_RIGHT,
            curses.KEY_UP,
            curses.KEY_DOWN,
            ESC
        ]:
            key = prev_key
        
        y = snake[0][0]
        x = snake[0][1]
        
        calculate_next_coordinates(key, snake, x, y, direction, win)


        # if snake runs over itself
        if snake[0] in snake[1:]: 
            # check if user hits left when it moves right
            if key == curses.KEY_LEFT and prev_key == curses.KEY_RIGHT:
                # if so, do not break, do nothing
                pass
            # check if user hits right when it moves left
            elif key == curses.KEY_RIGHT and prev_key == curses.KEY_LEFT:
                pass
            # check if user hits up when it moves down
            elif key == curses.KEY_UP and prev_key == curses.KEY_DOWN:
                pass
            # check if user hits down when it moves up
            elif key == curses.KEY_DOWN and prev_key == curses.KEY_UP:
                pass
            else:
                lives -= 1
                # if lives == 0:
                #     game_over(score)
                # break
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
        win.addch(snake[0][0], snake[0][1], '#')


    game_over(score)


main()