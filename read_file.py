import os
import time
from music import music
from threading import Thread
from video_display import videos


def read():
    while True:
        x = -1
        y = -1
        for i in range(6572):
            x = x + 1
            y = y + 1
            file = open(f"D:\\Project BadApple\\image\\frame{x}.txt", "r")
            content = file.read()
            time.sleep(0.029)
            print(content)
            file.close()


t3 = Thread(target=videos)
t3.start()    
t2 = Thread(target=music)
t2.start()
t1 = Thread(target=read)
t1.start()

        
        




