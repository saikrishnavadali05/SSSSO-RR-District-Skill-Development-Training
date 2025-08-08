import cv2


img = cv2.imread('image.jpg')  
cv2.imshow('Displayed Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Output:
# Displayed image in  awindow named 'Displayed Image'


