# Bad-Apple-and-bad-code
After seeing [SetuMar's](https://www.youtube.com/watch?v=tjSRx2eydwk) video, I really felt inspired and wanted to make one myself.  
So here's my janky and less intuitive way of playing Bad Apple with python.  
Also, I will leave link at the end of each step to a bunch of youtube videos based on the steps.  
  
  
# All the modules you'll need:
* __OpenCV__: ` pip install opencv-python`
* __pywhatkit__: `pip install pywhatkit`
* __pygame__: `pip install pygame`
* __os__: Built-in
* __time__: Built-in
* __threading__: Built-in
* __numpy__: `pip install numpy`  
  
# Step-by-step explanation(not very good)
* __Step 1__: Splitting video into individual frame  
Playing the video from file with OpenCV and splitting them into individual frame
`cap = cv2.VideoCapture("Video/Badapple.mp4")`  
(path-of-video/video's-name), I recommend saving everything in a project folder for easier access. Since my video is in a folder called "Video", I specify the folder name first but if your video is saved in the project folder and not inside another folder, you can straight up specify the video's name instead.  
`if not os.path.exists('data'):`  This line of code will check if a folder named 'data' existed.  
    `os.makedirs('data')` If not, it will make one  
`name = './data/frame' + str(currentFrame) + '.jpg'` This line will save all the current frame as a jpg file and put them in a 'data' folder  
    `print ('Creating...' + name)`
    `cv2.imwrite(name, frame)`  
[Video](https://www.youtube.com/watch?v=uL-wCzVMPsc&list=LL&index=2)  


* __Step 2__: Converting each frame into a text file or ascii_art  
You can use Pillow opposed to pywhatkit to convert those frames into images  
`pywhatkit.image_to_ascii_art(f"D:\\Project BadApple\\data\\frame{x}.jpg",f"D:\\Project BadApple\\image\\frame{y}"`  
With pywhatkit module, we can convert all the frame into ascii_art or text. First we specify the location of where we store our frames, then we specify where we want to store our new converted image.  
Ex: (Project-folder\\frames-folder\\frames-name),(Project-folder\\ascii_art-folders\\ascii_art-file-name)
__P.S Double backslash are needed for python to read our code.__  
[Video](https://www.youtube.com/watch?v=_HX0KSx93gQ&list=LL&index=3&t=244s)  
  
  
* __Step 3__: Playing the audio  
pygame module were use to play the audio, however you can use any other module you'd like.  
`pygame.init()` This line of code initialize all the pygame module, this is needed in order for the other command to work.  
`sound = pygame.mixer.Sound("BadappleAud.mp3")` We specify the audio's name in this function, mine is "BadappleAud.mp3"  
`while pygame.mixer.get_busy():`
    `pygame.time.delay(100)` This while loop check if the audio is playing, if it is, we delay it by 100ms  
  
    
* __Step 4__: Displaying the video  











