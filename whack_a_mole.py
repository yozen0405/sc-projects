from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

# Constant controls the pause time of the animation
DELAY = 100

# Global variables
window=GWindow(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,title='whack a mole')
score=0
score_label=GLabel('Score:'+str(score))
score_label.font='-50'
window.add(score_label,0,score_label.height+10)
# TODO:


def main():
    onmouseclicked(hit)
    while True:
        mole=GImage('mole.jpeg')
        mole_x=random.randint(0,window.width-mole.width)
        mole_y=random.randint(0,window.height-mole.height)
        window.add(mole,mole_x,mole_y)
        pause(DELAY)


def hit(event):
    maybe_obj=window.get_object_at(event.x,event.y)
    global score
    if maybe_obj!=None and maybe_obj!= score_label:
        window.remove(maybe_obj)
        score+=1
        score_label.text ='Score:' + str(score)

if __name__ == '__main__':
    main()
