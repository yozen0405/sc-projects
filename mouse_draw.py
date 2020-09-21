"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the pen stroke
SIZE = 30

window=GWindow()


def main():
	onmousedragged(draw)


def draw(event):
	if event.x>window.width//2:
		stroke=GOval(SIZE,SIZE)
		stroke.color='black'
		stroke.filled=True
		stroke.fill_color=stroke.color
	else:
		stroke = GOval(SIZE, SIZE)
		stroke.color = 'blue'
		stroke.filled = True
		stroke.fill_color = stroke.color
	for i in range(2):
		window.add(stroke, event.x + SIZE // 2, event.y + SIZE // 2)


if __name__ == '__main__':
	main()
