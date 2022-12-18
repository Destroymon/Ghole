import time
import cv2

from pygame import mixer

mixer.init()
mixer.music.load('D:/Alexey/Desktop/Проекты/Ghole/TK_from_Ling.mp3')
mixer.music.play()

a = 1000
while a > 0:
    print(f"{a} - 7 = {a - 7}")
    a -= 7
    time.sleep(0.1)

    if a < 0:
        mypath = 'shounen.jpg'
        img = cv2.imread(mypath, 1)
        cv2.imshow('', img)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()
        print("Я ГУЛЬ")

