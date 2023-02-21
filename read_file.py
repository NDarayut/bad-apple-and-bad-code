import os
import time
from music import music
from threading import Thread
from video_display import videos

#This is where all the text and video and sound will be display

def read(): #This function allow us to open and read each individual .txt file(the one we convert in image.py)
    con = True
    while con:
        x = -1
        y = -1
        for i in range(6572): #Since there are 6571 frame in total we set the range to 6572 and set x,y to -1
            x = x + 1          
            y = y + 1
            file = open(f"D:\\Project BadApple\\image\\frame{x}.txt", "r")#We locate the file path and read it with the open function
            content = file.read()
            time.sleep(0.029) #Use to adjust the timing to match the audio and video display
            print(content)
            file.close()
            if x == 6571: #Once x reaches 6571 the condition will turn False to stop the while loop
                con = False


t3 = Thread(target=videos) #Threading use to run all 3 function at the same time
t3.start()    
t2 = Thread(target=music)
t2.start()
t1 = Thread(target=read)
t1.start()

        
        




