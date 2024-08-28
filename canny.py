import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    frame = cv2.GaussianBlur(frame,(5,5),0)

    frame = cv2.Canny(frame,50,80)

    cv2.imshow('Live cam', frame)
    
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
