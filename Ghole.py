import time
import cv2
from playsound import playsound

playsound(
    '/Users/gvozdevalexey/Downloads/TK_from_Ling_Tosite_Sigure_-_UNRAVEL_ost_Tokyo_Ghoul_Tokijjskijj_gul_OP_64191680.mp3',
    False)

a = 1000
while a > 0:
    print(f"{a} - 7 = {a - 7}")
    a -= 7
    time.sleep(0.1)

    if a < 0:
        img = cv2.imread(
            '/Users/gvozdevalexey/Downloads/shounen-red-eyes-human-monster-tokyo-ghoul-ken-kaneki-ghoul.jpg', 0)
        cv2.imshow('', img)
        cv2.waitKey(1)
        time.sleep(5)

