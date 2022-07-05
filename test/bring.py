import pyautogui as pya
from PIL import ImageGrab

def color_def(a):
    result = 0
    jubsu   = (210, 0, 255) 
    daegi   = (1, 150, 245) 
    jongryo = (0, 30, 255)  

    screen = ImageGrab.grab() 
    rgb = screen.getpixel(a) 

    if rgb == jubsu:     result = 1   
    elif rgb == daegi:   result = 2 
    elif rgb == jongryo: result = 3   
    else : result = 0             
    return result


