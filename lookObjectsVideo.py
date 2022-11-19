import numpy as np
import cv2

import lookforObjects as lookModule


# So I simply pass 0 (or -1).
# You can select the second camera by passing 1 and so on. 
# After that, you can capture frame-by-frame.
# But at the end, don’t forget to release the capture.

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # orientations and centers are lists
    orientations, centers, out_img = lookModule.getOrientationsAndCenters(frame)

    # Display the new image
    cv2.imshow('Out Image', out_img)

    #Print orientation and center for the first object found in the image
    if not orientations:
        print('Empty list')
    else:
        print(orientations[0])
        print(centers[0])
   
    # 1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
    # 2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed. Since the OS has a minimum time between switching threads, the function will not wait exactly 1 ms, it will wait at least 1 ms, depending on what else is running on your computer at that time.
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Ctrl + C in terminal to stop running
