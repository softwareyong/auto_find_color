import pyautogui as pya 
from PIL import ImageGrab
import bring as rgb 
from playsound import playsound

print("Running")     
pya.screenshot('sosok.png', region=(21, 106, 36, 20))  
i = 1

while(True):
    sosok = pya.locateCenterOnScreen('sosok.png') 
    pos_x = sosok.x
    pos_y = sosok.y+(i*23) 
    pos = (pos_x, pos_y)

    color = rgb.color_def(pos)

    if(color == 1):
        playsound("1.mp3")  
    elif(color == 2):
        playsound("2.mp3")
    elif( (color == 3) or (i == 20) ):
        i = 0 
    
    i += 1
    
    
   
   


  

 
