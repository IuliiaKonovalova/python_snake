import curses


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


# main logic
score = 0
while True:
    event = win.getch()
    if event == 27:
        break
    
curses.endwin()

print("Game Over")
print(f"Final Score = {score}")