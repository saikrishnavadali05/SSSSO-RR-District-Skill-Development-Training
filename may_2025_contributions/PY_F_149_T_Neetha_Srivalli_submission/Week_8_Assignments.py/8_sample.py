import cv2

img = cv2.imread('image.jpg')  # Replace with your image path
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Output:
# Displayed graysacle image in a window named 'Grayscale Image'
