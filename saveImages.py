import cv2
import os
import imutils


dataPath = '../persp_set/class_a/' #Cambia a la ruta donde hayas almacenado Data


# if not os.path.exists(personPath):
#     print('Carpeta creada: ',personPath)
#     os.makedirs(personPath)

cap = cv2.VideoCapture(0)
START_COUNT = 1200
NUM_IMAGES = 200
count = START_COUNT

while True:

    ret, frame = cap.read()
    if ret == False: break
    #frame =  imutils.resize(frame, width=640)
    cv2.imwrite(dataPath + '/botella_{}.jpg'.format(count),frame)
    cv2.imshow('frame',frame)
    count = count + 1
    cv2.waitKey(300)
    if count >= (START_COUNT+NUM_IMAGES):
        break

cap.release()
cv2.destroyAllWindows()
