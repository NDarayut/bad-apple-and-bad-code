import cv2 as cv
import time

capture = cv.VideoCapture("Video/Badapple.mp4")

def videos():
    def rescale_frame(frames, scale=0.75):
        width = int(frames.shape[1] * scale)
        height = int(frames.shape[0] * scale)
        dimension = (width,height)
        return cv.resize(frames, dimension, interpolation=cv.INTER_AREA)



    while True:
        time.sleep(0.007)
        isTrue, frames = capture.read()
        frame_resized = rescale_frame(frames, scale=.5)
        
        cv.imshow("Video resized", frame_resized)
        #cv.imshow("Video", frames)
        if cv.waitKey(20) & 0xFF==ord("q"):
            break

    capture.releae()
    cv.destroyAllWindows()
