import numpy as np
import cv2
 
 # ---------------------------------------------------------------
 # 노트북에 연결된 캠을 이용한 영상처리 예제
 # 'q'를 눌러서 프로그램을 종료할 수 있다.
 # ---------------------------------------------------------------
 
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
     
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()