import cv

img = cv.imread('image.jpg')  # Replace with your image path
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges =cv.Canny(gray, 100, 200)

cv.imshow('Edge Detected Image', edges)
cv.waitKey(0)
cv.destroyAllWindows()

#Output:
# Displayed edge detected image in a window named 'Edge Detected Image'