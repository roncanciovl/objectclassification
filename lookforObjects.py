# Principal component analysis method for orientation calculation on objects inside an image
# https://automaticaddison.com/how-to-determine-the-orientation-of-an-object-using-opencv/

import cv2 as cv
from math import atan2, cos, sin, sqrt, pi
import numpy as np
 
def drawAxis(img, p_, q_, color, scale):
    p = list(p_)
    q = list(q_)
  
    ## [visualization1]
    angle = atan2(p[1] - q[1], p[0] - q[0]) # angle in radians
    hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))
  
    # Here we lengthen the arrow by a factor of scale
    q[0] = p[0] - scale * hypotenuse * cos(angle)
    q[1] = p[1] - scale * hypotenuse * sin(angle)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
  
    # create the arrow hooks
    p[0] = q[0] + 9 * cos(angle + pi / 4)
    p[1] = q[1] + 9 * sin(angle + pi / 4)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
  
    p[0] = q[0] + 9 * cos(angle - pi / 4)
    p[1] = q[1] + 9 * sin(angle - pi / 4)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
    ## [visualization1]



def getOrientation(pts, img):
    #listofOrientations = []
    ## [pca]
    # Construct a buffer used by the pca analysis
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
      data_pts[i,0] = pts[i,0,0]
      data_pts[i,1] = pts[i,0,1]
  
    # Perform PCA analysis
    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
  
    # Store the center of the object
    cntr = (int(mean[0,0]), int(mean[0,1]))
    ## [pca]
  
    ## [visualization]
    # Draw the principal components
    cv.circle(img, cntr, 3, (255, 0, 255), 2)
    p1 = (cntr[0] + 0.02 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.02 * eigenvectors[0,1] * eigenvalues[0,0])
    p2 = (cntr[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0])
    drawAxis(img, cntr, p1, (255, 255, 0), 1)
    drawAxis(img, cntr, p2, (0, 0, 255), 5)
  
    angle = atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians
    ## [visualization]
  
    # Label with the rotation angle
    label = "  Rotation Angle: " + str(-int(np.rad2deg(angle)) - 90) + " degrees"
    textbox = cv.rectangle(img, (cntr[0], cntr[1]-25), (cntr[0] + 250, cntr[1] + 10), (255,255,255), -1)
    cv.putText(img, label, (cntr[0], cntr[1]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
  
    return angle


# Return an empty list if no object found, otherwise return a list of orientation,
# a list of centers, and a new image with the contours, centers and orientation vectors
def getOrientationsAndCenters(img):
    listofOrientations = []
    listofCenters = []
    contours = getContours(img)
    for i, c in enumerate(contours):
      
        # Calculate the area of each contour
        area = cv.contourArea(c)
      
        # Ignore contours that are too small or too large
        # 3700, 100000  
        if area < 3700 or 100000 < area:
          continue
      
        # Draw each contour only for visualisation purposes
        cv.drawContours(img, contours, i, (0, 0, 255), 2)
      
        # Find the orientation of each shape
        #getOrientation(c, img)
        #print(getCenter(c, img))


        ## [pca]
        # Construct a buffer used by the pca analysis
        sz = len(c)
        data_pts = np.empty((sz, 2), dtype=np.float64)
        for i in range(data_pts.shape[0]):
          data_pts[i,0] = c[i,0,0]
          data_pts[i,1] = c[i,0,1]
      
        # Perform PCA analysis
        mean = np.empty((0))
        mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
      
        # Store the center of the object
        cntr = (int(mean[0,0]), int(mean[0,1]))
        listofCenters.append(cntr)
        ## [pca]
      
        ## [visualization]
        # Draw the principal components
        cv.circle(img, cntr, 3, (255, 0, 255), 2)
        p1 = (cntr[0] + 0.02 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.02 * eigenvectors[0,1] * eigenvalues[0,0])
        p2 = (cntr[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0])
        drawAxis(img, cntr, p1, (255, 255, 0), 1)
        drawAxis(img, cntr, p2, (0, 0, 255), 5)
      
        angle = atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians
        ## [visualization]
      
        # Label with the rotation angle
        label = "  Rotation Angle: " + str(-int(np.rad2deg(angle)) - 90) + " degrees"
        textbox = cv.rectangle(img, (cntr[0], cntr[1]-25), (cntr[0] + 250, cntr[1] + 10), (255,255,255), -1)
        cv.putText(img, label, (cntr[0], cntr[1]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
      
        listofOrientations.append(angle)
    return listofOrientations, listofCenters, img


def getCenter(pts, img):
    ## [pca]
    # Construct a buffer used by the pca analysis
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
      data_pts[i,0] = pts[i,0,0]
      data_pts[i,1] = pts[i,0,1]
  
    # Perform PCA analysis
    mean = np.empty((0))
    
    #The principal components of a collection of points in a real coordinate space
    #are a sequence of p unit vectors, where the i-th vector
    # is the direction of a line that best fits the data
    # while being orthogonal to the first i-1 vectors. 
    # Here, a best-fitting line is defined as one that minimizes
    # the average squared perpendicular distance from the points to the line.
    # The eigenvector is a vector that is associated with a set of linear equations.
    mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
  
    # Store the center of the object
    cntr = (int(mean[0,0]), int(mean[0,1]))
    ## [pca]
    return cntr 

# if any object return 1
def lookforAnyObject(img):

    pts = getContours(img)  
       ## [pca]
    # Construct a buffer used by the pca analysis
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
      data_pts[i,0] = pts[i,0,0]
      data_pts[i,1] = pts[i,0,1]
  
    # Perform PCA analysis
    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)

    if mean != np.empty((0)): 
      return 1
    else: 
      return 0

def getContours(img):
    # Convert image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Convert image to binary
    _, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    # Find all the contours in the thresholded image
    contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    return contours


def testOnlookforObjects():

    # Load the image
    img = cv.imread("./test_images/l2_g6.jpg")
    
    # Was the image there?
    if img is None:
        print("Error: File not found")
        exit(0)
      
    cv.imshow('Input Image', img)
    
    # Convert image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Convert image to binary
    _, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    # Find all the contours in the thresholded image
    contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    
    for i, c in enumerate(contours):
      
        # Calculate the area of each contour
        area = cv.contourArea(c)
      
        # Ignore contours that are too small or too large
        # 3700, 100000  
        if area < 3700 or 100000 < area:
          continue
      
        # Draw each contour only for visualisation purposes
        cv.drawContours(img, contours, i, (0, 0, 255), 2)
      
        # Find the orientation of each shape
        getOrientation(c, img)
        print(getCenter(c, img))
    
    cv.imshow('Output Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
      
    # Save the output image to the current directory
    #cv.imwrite("output_img.jpg", img)


if __name__ == "__main__":
    testOnlookforObjects() 