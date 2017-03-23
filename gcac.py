import sys
import time
import uinput

sleepTime = 100


def click():
	with uinput.Device(events) as device:
		uinput.BTN_LEFT

def autoClick(num):
	for i in range(0,num):
		click()
		time.sleep(sleepTime)


def main():
	if len(sys.argv) < 2:
		print "Usage: python gcac.py <number of clicks>"
	else:
		autoClick(int(sys.argv[1]))
	exit()
main()