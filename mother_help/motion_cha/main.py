# pip opencv-python 을 설치해야함
import pyautogui as pya 
from PIL import ImageGrab
import rgb_bring as rgb  
import time
from playsound import playsound

# b = pya.position()          
pya.screenshot('sosok.png', region=(31, 138, 24, 19))  #좌표의 사진을 찍는다 
i = 1

while(True):
    sosok = pya.locateCenterOnScreen('sosok.png') # 사진의 위치가 바껴도 소속의 x,y 좌표 계속 알려줌
    #pya.moveTo(sosok.x, sosok.y, 1)   # 1초동안 x,y 중앙 좌표로 이동 -> 상대이동으로 바꿔줘야함
    pos_x = sosok.x
    pos_y = sosok.y+(i*23) 
    pos = (pos_x, pos_y)

    color = rgb.color_def(pos)
    if(color == 1):
        playsound("1.mp3")  
        break
    elif(color == 2):
        playsound("2.mp3")
        break
    elif( (color == 3) or (i == 20) ):
        i = 0 
    
    i += 1
    # pos = (sosok.x, sosok.y + (i*23))    
    #time.sleep(0.1)
    pya.moveTo(pos_x, pos_y, 0.1) #23pixel 차이남 다음꺼랑   
    
    
# esc 키 들어올때까지 무한반복으로 바꾸기 
# 그 전꺼 기억해서 시간보고 시간에 따라 그냥 지금 시간하고 비교해서 넘기기    


  

 
