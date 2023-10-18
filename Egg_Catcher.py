from itertools import cycle
from random import *
from tkinter import *
from tkinter import font
from tkinter import messagebox
import time as t
import pygame as p

def run():
    eggs = []
    hearts = []





    def sound():
        p.mixer.init()
        eg = p.mixer.Sound('ec.mp3')
        eg.play()
        t.sleep(5)
    


    def create_egg():
        x = randrange(10, 750)
        y = 40
        new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
        eggs.append(new_egg)
        root.after(egg_interval,create_egg)

    def move_eggs():
        for egg in eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
            c.move(egg, 0, 10)
            if egg_y2 > canvas_height:
                egg_dropped(egg)
        root.after(egg_speed, move_eggs)    


    def egg_dropped(egg):
        eggs.remove(egg)
        c.delete(egg)
        lose_a_life()
        if lives_remaining == 0:
            messagebox.showinfo('Game Over', 'Final Score: ' + str(score))

            root.destroy()

    def lose_a_life():
        global lives_remaining
        lives_remaining -= 1
        c.itemconfigure(lives_text, text='Lives: '+ str(heart * lives_remaining))


    def check_catch():
        (catcher_x, catcher_y, catcher_x2,catcher_y2) = c.coords(catcher)
        for egg in eggs:
            (egg_x, egg_y, egg_x2,egg_y2) = c.coords(egg)
            if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
                eggs.remove(egg)
                c.delete(egg)
                increase_score(egg_score)

        root.after(100, check_catch)        


    def increase_score(points):
        global score, egg_speed, egg_interval
        score += points
        egg_speed = int(egg_speed * dificulty_factor)
        egg_interval = int(egg_interval * dificulty_factor)

        c.itemconfigure(score_text, text='Score: '+ str(score))


    def create_heart():
        x = randrange(10, 750)
        y = 40
        new_heart = life_heart
        hearts.append(new_heart)
        root.after(egg_interval - 100,create_heart)


    def check_catch_life():
        (catcher_x, catcher_y, catcher_x2,catcher_y2) = c.coords(catcher)
        for life_heart in heart:
            (life_heart_x, life_heart_y, life_heart_x2, life_heart_y2) = c.coords(life_heart)
            if catcher_x < life_heart_x and life_heart_x2 < catcher_x2 and catcher_y2 - life_heart_y2 < 40:
                hearts.remove(life_heart)
                c.delete(life_heart)
                increase_life()

        root.after(100, check_catch_life)        

    def increase_life():
        global lives_remaining
        lives_remaining += 2
        c.itemconfigure(lives_text, text='Lives: '+ str(heart * lives_remaining))



    def move_heart():
        for life_heart in hearts:
            (life_heart_x, life_heart_y, life_heart_x2, life_heart_y2) = c.coords(life_heart)
            c.move(life_heart, 0, 10)
            if life_heart_y2 > canvas_height:
                life_dropped(life_heart)
        root.after(egg_speed + randrange(10, 1000), move_heart)

    def life_dropped(life):
        hearts.remove(life)
        c.delete(life)
        
        
    def move_left(event):
        (x1, y1, x2, y2) = c.coords(catcher)
        if x1 > 0:
            c.move(catcher,-20, 0)

    def move_right(event):
        (x1, y1, x2, y2) = c.coords(catcher)
        if x2 < canvas_width:
            c.move(catcher, 20, 0)

    gaming = True

    canvas_width = 1000
    canvas_height = 400

    root = Tk()
    root.title('Egg Catcher')

    c = Canvas(root, width=canvas_width,height=canvas_height, background='deep sky blue')

    c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height +5, fill='sea green', width=0)
    c.create_oval(-80,-80,120,120,fill='orange', width=0)


    c.pack()

    color_cycle = cycle(['light blue','light yellow', 'light pink','light cyan'])


    life_heart = u'\u2764' 

    egg_width = 45
    egg_height = 55
    egg_score = 10
    egg_speed = 500
    egg_interval = 4000
    dificulty_factor = 0.95


    catcher_color = 'red'
    catcher_width = 100
    catcher_height = 100

    catcher_start_x = canvas_width / 2 - catcher_width / 2
    catcher_start_y = canvas_height - catcher_height - 2
    catcher_start_x2 = catcher_start_x + catcher_width
    catcher_start_y2 = catcher_start_y + catcher_height


    catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, start=200, extent = 140, style='arc', outline = catcher_color, width=10)

    game_font = font.nametofont('TkFixedFont')
    game_font.config(size=18)

    score = 0
    score_text = c.create_text(10,10,anchor='nw',font=game_font,fill='darkblue',text='Score: ' + str(score))

    lives_remaining = 3
    heart = u'\u2764'

    lives_text = c.create_text(canvas_width-100,10,anchor='ne',font=game_font,fill='darkblue',text='Lives ' + str(heart * lives_remaining))


    c.bind('<Left>', move_left)
    c.bind('<Right>', move_right)
    c.focus_set()

    root.after(2,sound)
    root.after(1000, create_egg)
    root.after(1000, move_eggs)
    root.after(1000, check_catch)

    root.after(1000, create_heart)
    root.after(1000, move_heart)
    root.after(1000, check_catch_life)


    root.mainloop()

