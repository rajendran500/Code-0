import cv2 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    
    
    if len(faces) > 0: 
        print("It's a human ")
        for (x,y,w,h) in faces: 
            cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),2) 
    else:
        print("Its not a human ")
    cv2.imshow ('Face Detection', frame) 
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release() 
cv2.destroyAllWindows() 
