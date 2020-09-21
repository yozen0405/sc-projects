"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 1


window=GWindow()


def main():
	onmouseclicked(hole_punch)


def hole_punch(event):
	hole=GOval(SIZE,SIZE)
	hole.filled=True
	window.add(hole,event.x-SIZE//2,event.y-SIZE//2)





if __name__ == '__main__':
	main()
