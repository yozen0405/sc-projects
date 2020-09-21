"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved

# This constant controls the size of the GRect
SIZE = 100

w=GWindow()
r=GRect(SIZE,SIZE)
r.filled=True


def main():
	w.add(r,0,0)
	onmousemoved(reset)


def reset(event):
	r.x=event.x-SIZE//2
	r.y=event.y-SIZE//2



if __name__ == '__main__':
	main()
