
#!/usr/bin/python
# -*- coding: utf-8 -*-

from ezprint import *
from tkinter import *
from time import *

import random
import threading

firstFrame = None
c = None
second = 0.05
bar = 0


def input_bar():
	global bar

	bar = int(input('Input bar: '))


def start_draw():
	time_tread = threading.Thread(target=draw_point)
	time_tread.start()


def draw_point():
	global firstFrame

	firstFrame.geometry(str(bar) + 'x30')
	for x in range(1, int(bar)):
		c.create_rectangle(x, 0, x, 30, fill='blue', outline='blue', width=1)
		sleep(second)


def main():
	global c
	global val
	global firstFrame

	firstFrame = Tk()
	
	firstFrame.title('Progress Bar')

	firstFrame.resizable(0, 0)

	c = Canvas(firstFrame, width=bar, height=30, bg='white')

	c.pack()

	start_draw()

	firstFrame.mainloop()


if __name__ == '__main__':
	input_bar()
	main()