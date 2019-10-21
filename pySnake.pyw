import tkinter as tk
from random import randint

def newFruit():
    fruit = randint(0,99)
    while(fruit in snake):
        fruit = randint(0,99)
    return fruit

def sort(list):
    return list[randint(0,len(list)-1)]

root = tk.Tk()
root.geometry('300x330')
root.title('Snake Game')
root['bg'] = 'grey'
root.resizable(False, False)

blocks = []
for i in range(100):
    blocks.append(tk.Frame(root, width=29, height=29, bg='white'))

# map generation
countY = 0
countX = 0
for i in range(0, 100):
    if (i % 10 == 0 and i != 0):
        countY += 30
        countX = 0
    blocks[i].place(x=countX, y=countY)
    countX += 30

# points counter
points = 0
points_var = tk.Label(root, text='Points: {}'.format(points))
points_var.place(x=10, y=305)

# game variables
snake = [randint(0,99)]
fruit = newFruit()

# game start
while(True):
    blocks[fruit].config(bg='red')
    for i in snake:
        blocks[i].config(bg = 'green')
    break

root.mainloop()