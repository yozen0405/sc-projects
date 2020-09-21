"""
File: bouncing_rect.py
Name:Albert
------------------------
This file shows how to make a simple 
animation by campy library
"""

from campy.graphics.gobjects import GOval,GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 100

# This controls the pause time (in millisecond) for the animation
DELAY = 20


def main():
	window=GWindow()
	rect=set_up_r()
	window.add(rect,(window.width-rect.width)//2,(window.height-rect.height)//2)
	vx=5
	while True:
		rect.move(vx,0)
		if rect.x<=0 or rect.x+rect.width>=window.width:
			vx=-vx
			if vx>0:
				rect.color = 'purple'
				rect.filled = True
				rect.fill_color = rect.color
			else:
				rect.color = 'green'
				rect.filled = True
				rect.fill_color = rect.color
		pause(DELAY)


def set_up_r():
	rect=GRect(SIZE,SIZE)
	rect.color='green'
	rect.filled=True
	rect.fill_color=rect.color
	return rect



if __name__ == '__main__':
	main()
