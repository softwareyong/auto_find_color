# pillow 모듈 깔아야함 imageGrab함수가 
import pyautogui as pya
from PIL import ImageGrab

def color_def(a):
    result = 0
    jubsu   = (210, 0, 255) #접수
    daegi   = (1, 150, 245) #대기
    jongryo = (0, 30, 255)  #종료 

    screen = ImageGrab.grab() # 화면 찍기
    rgb = screen.getpixel(a) # rgb에 스크린에서 찍은화면중 원하는 좌표에 색깔뽑기

    if rgb == jubsu:     result = 1   # 접수 -> 1
    elif rgb == daegi:   result = 2   # 대기 -> 2
    elif rgb == jongryo: result = 3   # 종료 -> 3
    else : result = 0              # 이거랑 다르면    예외처리  3   오류라고 출력해야함 
    return result


