import cv2
from tkinter import *
import tkinter.messagebox


while True:
    try:
        #print(check) # Prints True if the webcam runs
        #cv2.imshow("Capture WebCam", frame) #Shows live feed!!
        key = input("Take Picture with 's' or exit with 'q': ")
        if key == 's':
            key = cv2.waitKey(1)
            webcam = cv2.VideoCapture(0)
            check, frame = webcam.read()
            root = Tk()
            cv2.imwrite(filename='catch_before.jpg', img=frame)
            tkinter.messagebox.showinfo('You have been pwned!', 'Say Cheese your Picture has been taken!')
            root.destroy()
        if key == 'q':
            print("Turning off camera!")
            webcam.release()
            print("WebCam is offline...")
            print("Live feed ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera!")
        webcam.release()
        print("WebCam is offline...")
        print("Live feed ended.")
        cv2.destroyAllWindows()
        break