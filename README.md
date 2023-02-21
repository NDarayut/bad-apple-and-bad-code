# Bad-Apple-and-bad-code
After seeing [SetuMar's](https://www.youtube.com/watch?v=tjSRx2eydwk) video, I really felt inspired and wanted to make one myself.  
So here's my janky and less intuitive way of playing Bad Apple with python.  
  
  
# All the modules you'll need:
* __OpenCV__: ` pip install opencv-python`
* __pywhatkit__: `pip install pywhatkit`
* __pygame__: `pip install pygame`
* __os__: Built-in
* __time__: Built-in
* __threading__: Built-in
* __numpy__: `pip install numpy`  
  
# Step-by-step explanation(not very good)
__Step 1__: Splitting video's frame into individual frame  
`cap = cv2.VideoCapture("Video/Badapple.mp4")` (path-of-video/video's-name), I recommend saving everything in a project folder for easier access. since my video is in a folder called Video, i specify the folder name first but if your video is saved in a project folder and not inside another folder, you can straight up specify the name instead.  
`if not os.path.exists('data'):`  This line of code will check if a folder named 'data' existed.  
    `os.makedirs('data')` If not, it will make one  
`name = './data/frame' + str(currentFrame) + '.jpg'` This line will save all the current frame as a jpg file and put them in a 'data' folder
    `print ('Creating...' + name)`
    `cv2.imwrite(name, frame)`

__Step 2__: Converting each frame into a text file or ascii_art  
`pywhatkit.image_to_ascii_art(f"D:\\Project BadApple\\data\\frame{x}.jpg",f"D:\\Project BadApple\\image\\frame{y}"`  
With pywhatkit module, we can convert all the frame into ascii_art or text. First we specify the location of where we store our frames, then we specify where we want to store our new converted image. (Project-folder\\frames-folder\\frames-name),(Project-folder\\)
P.S Double backslash are needed for python to read our code.







