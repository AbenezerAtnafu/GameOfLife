from tkinter import *
from Box import Box
import time

def check_all():
	for i in box.grid:
		for cell in i:
			if cell.is_alive():
				board[cell.row][cell.col]["bg"] = "red"
			else:
				board[cell.row][cell.col]["bg"] = "white"
	room.update()
				
def change(cell):
	if cell.is_alive():
		cell.set_alive(0)
		board[cell.row][cell.col]["bg"] = "white"
	else:
		cell.set_alive(1)
		board[cell.row][cell.col]["bg"] = "red"
	
def begin():
	while 1:
		box.step()
		check_all()
		time.sleep(0.5)


row = int(input("how many rows? "))
col = int(input("how many cols? "))

board = [[0 for i in range(col)] for j in range(row)]
box = Box(row, col)
room = Tk()

playground = Frame()

for x in range(row):
	for y in range(col):
		board[x][y] = Button(playground, text="", font=('Verdana',10), bg="white", width=3, command = lambda place = box.grid[x][y]: change(place))
		board[x][y].grid(row = x, column=y)
		
done = Button(text='Start', command=begin)
tell = Label(text = "Game of Life")
playground.grid(row=1, column=0)
done.grid(row=2, column=0)
tell.grid(row=0, column=0)
mainloop()
