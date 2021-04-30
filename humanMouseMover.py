from pyclick import HumanClicker
import time
import random


# initialize HumanClicker object
print("Human like mouse simulating start....")

hc = HumanClicker()

# move the mouse to position (100,100) on the screen in approximately 2 seconds
while True:	
	hc.move((random.randint(0,1500),random.randint(0,900)),random.randint(0,5))
	print("sleep 30s ..........................")
	time.sleep(35) 


# mouse click(left button)
