from mss import mss
from time import sleep
import win32gui 
import pyautogui
box = (230,480,235,481) 
act = mss()


def screen_location():
	while True:
	
		print(win32gui.GetCursorPos())
		sleep(1)



def trex():
	while True:
		frame = act.grab(box) 

		if frame.pixel(2,0)[0]<100 and frame.pixel(2,0)[0]>50 or frame.pixel(1,0)[0]<100 and frame.pixel(1,0)[0]>50 or frame.pixel(3,0)[0]<100 and frame.pixel(3,0)[0]>50 :
			print("jump")
			pyautogui.press("space")
			sleep(0.05)        
		else:
			pass 


		
		 
			
