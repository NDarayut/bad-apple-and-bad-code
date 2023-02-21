import cv2 as cv
import time

capture = cv.VideoCapture("Video/Badapple.mp4") #We specify the file path, mine is in a folder called Video

def videos():
    def rescale_frame(frames, scale=0.75): #You can adjust the video scale to your liking, 0.75 being 75% and 1 being 100%
        width = int(frames.shape[1] * scale)
        height = int(frames.shape[0] * scale)
        dimension = (width,height)
        return cv.resize(frames, dimension, interpolation=cv.INTER_AREA)



    while True:
        time.sleep(0.007) 
        isTrue, frames = capture.read()
        frame_resized = rescale_frame(frames, scale=.5)
        
        cv.imshow("Video resized", frame_resized) #This function display the video
        if cv.waitKey(20) & 0xFF==ord("q"): #The video will break when you press "q" or you can set it to any key
            break

    capture.releae()
    cv.destroyAllWindows()
