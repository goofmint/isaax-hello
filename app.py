from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyS0')
print "Start blinking D4"
while True:
    board.digital[4].write(1)
    sleep(0.5)
    board.digital[4].write(0)
    sleep(0.5)
