import time # for delaying if needed
import curses # for wasd controlling
from motor import Ordinary_Car  

SPEED = 2000 # set car speed

def main(stdscr):

    curses.noecho() # prevents key presses from appearing in terminal
    curses.cbreak() # no line buffering (liek hitting enter)
    stdscr.nodelay(True) # stops input if key isn't currently being pressed

    # initalizing motor controller
    car = Ordinary_Car()

    try:
        while True:
            key = stdscr.getch()

            if key == -1:
                # if no key is being pressed - stop car
                car.set_motor_model(0,0,0,0)

            if key == ord('w'):
                # if w is pressed - all wheels spin forward
                car.set_motor_model(SPEED,SPEED,SPEED,SPEED) # Forward

            elif key == ord('s'):
                # if s is pressed - all wheels spin backwards
                car.set_motor_model(-SPEED,-SPEED,-SPEED,-SPEED) # Back

            elif key == ord('a'):
                # if a is pressed - left wheels spin backward, right wheels spin forward
                car.set_motor_model(-SPEED,-SPEED,SPEED,SPEED) # Left

            elif key == ord('d'):
                # if d is pressed - left wheels spin forward, right wheels spin backward
                car.set_motor_model(SPEED,SPEED,-SPEED,-SPEED) # Right

            elif key == ord(' '):
                #if spacebar? is pressed - all wheels stop spinning
                car.set_motor_model(0,0,0,0)    # Stop

            elif key == ord('q'):
                # if q is pressed - quit
                break

            time.sleep(0.05)

    finally:
        # this makes sure the car stops and doesn't go flying when the script ends
        car.set_motor_model(0,0,0,0)

if __name__=='__main__':
    curses.wrapper(main)