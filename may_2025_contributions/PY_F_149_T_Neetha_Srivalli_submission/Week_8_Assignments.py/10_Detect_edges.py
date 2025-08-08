#     import cv2    --Importing OpenCV library

#     img = cv2.imread('image.jpg')            -- Replace with your image path
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    --Convert to grayscale
#     edges =cv2.Canny(gray, 100, 200)     --Detect edges using canny edge detection

#     cv2.imshow('Edge Detected Image', edges)   --Display edge detected image
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#Output:
# Displayed edge detected image in a window named 'Edge Detected Image'