import cv2
import tkinter as tk
import tkinter.font as font
import random
# show outcome
def neep():
    wind = tk.Tk()
    wind.title("Fortune")
    wind.geometry("400x100")
    l = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
    k = random.randrange(0, 5)
    g = tk.Label(wind, text=l[k])
    g.config(font=("Arial", 50))
    g.pack()
    wind.mainloop()
# scan face
def scan():
    win.destroy()
    while True:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            print(x,y,w,h)
            break
        break
    neep()


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# start button
win = tk.Tk()
win.title("Fortune")
win.geometry("300x200")
myFont = font.Font(family='Arial', size=30)
but = tk.Button(win,text="測運勢",width=30,height=10)
but['font'] = myFont
but.config(command=scan)
g = tk.Label(win, text = "若單日多次嘗試必不靈驗")
g.config(font =("Arial", 14))
g.pack()
but.pack()
win.mainloop()
