import cv2
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)

while True:
    try:
        check, frame = webcam.read()
        #print(check) # Prints True if the webcam runs
        cv2.imshow("Capture WebCam", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
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