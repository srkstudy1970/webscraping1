import cv2
# This code finally works ( I down loaded the latest Open CV for Win file from website https://sourceforge.net/projects/opencvlibrary/files/
# copied the latest version of the xml files into the project folder and gave the relative path to the files in the program below and it worked.
# looks like my cam is very old the face and eyes are not being dedected continiously, they are being detected intermittently

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

if face_cascade.empty():
   print("face cascade is empty")
   quit()


cap = cv2.VideoCapture(0)

while (True):
    print("inside while loop")
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(gray,1.3,5)
    print("inside while loop - Step 2- vaishu")
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color= img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k== 27:
        break

    '''
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    '''
cap.release()
cv2.destroyAllWindows()