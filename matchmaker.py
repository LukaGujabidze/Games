import random as r
import time
from tkinter import Tk, Button, DISABLED


# this is a function to hide and then show sybols

def show_symbol(x, y):
    global first
    global previus_X, previus_Y

    buttons[x, y]['text'] = button_symbols[x,y]
    buttons[x, y].update_idletasks()


    if first:
        previus_X = x
        previus_Y = y
        first = False

    elif previus_X != x or previus_Y != y:
        if buttons[previus_X, previus_Y]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previus_X, previus_Y]['text'] = ''
            buttons[x, y]['text'] = ''

        else:
            buttons[previus_X, previus_Y]['command'] = ''
            buttons[x, y]['command'] = ''

        first = True

                


# this are variebles that create GUI
root = Tk()
root.title('Matchmaker')
root.resizable(width=True, height=True)

first = True

buttons = {}
button_symbols = {}

previus_X = 0
previus_Y = 0


# this is list of unicode sybols

symbols = [u'\u2702',u'\u2702',u'\u2602',u'\u2602',u'\u2708',u'\u2708',u'\u2764',u'\u2764',u'\u270F',u'\u270F',u'\u2716',u'\u2716',
           u'\u2714',u'\u2714',u'\u2600',u'\u2600',u'\u2601',u'\u2601',u'\u2658',u'\u2658',u'\u267B',u'\u267B',u'\u26A0',u'\u26A0',
           u'\u2744', u'\u2744',u'\u27B0',u'\u27B0',u'\u2747',u'\u2747']

r.shuffle(symbols)

for x in range(6):
    for y in range(5):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=10, height=10)
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

root.mainloop()

