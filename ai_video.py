import numpy as np
import cv2
from ai import *


# So I simply pass 0 (or -1).
# You can select the second camera by passing 1 and so on. 
# After that, you can capture frame-by-frame.
# But at the end, don’t forget to release the capture.

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    prediction = None
    prediction = detectObjectAI(frame)

    # 1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
    # 2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed. Since the OS has a minimum time between switching threads, the function will not wait exactly 1 ms, it will wait at least 1 ms, depending on what else is running on your computer at that time.
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Ctrl + C in terminal to stop running
