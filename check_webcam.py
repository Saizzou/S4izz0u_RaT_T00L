import cv2
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)

try:
    check, frame = webcam.read()
    if check == True:
        print("Victim has an active WebCam!!!")
except:
    print("No WebCam found!")