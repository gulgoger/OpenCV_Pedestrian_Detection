import cv2
import imutils

cap = cv2.VideoCapture("C:\\Users\\asus_\\Documents\\Projects\\OPENCV\\opencv_pedestrian_detection\\test.mp4")

while True:
    ret, frame = cap.read()
    if ret==False:
        break

    frame = imutils.resize(frame,400)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (coordinate,_) = hog.detectMultiScale(frame,winStride=(4,4),padding=(8,8),scale=1.05)

    color = (0,255,0)
    thickness = 5

    for (x,y,w,h) in coordinate:
        cv2.rectangle(frame, (x,y),(x+w,y+h),color,thickness)

    cv2.imshow("Original Frame",frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()










