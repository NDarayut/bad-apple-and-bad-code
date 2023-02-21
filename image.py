import pywhatkit
x = -1
y = -1
for i in range(6572):
    x = x + 1
    y = y + 1
    pywhatkit.image_to_ascii_art(f"D:\\Project BadApple\\data\\frame{x}.jpg",f"D:\\Project BadApple\\image\\frame{y}")
    

