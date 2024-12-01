import cv2
import numpy as np

# Initialize list to store points
points = []

# Mouse callback function to capture points
def select_point(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point selected: {x}, {y}")

# Load the image
image = cv2.imread('tennis2.jpeg')
cv2.imshow("Image", image)

# Set the mouse callback to capture points
cv2.setMouseCallback("Image", select_point)

# Wait until 4 points are selected
while len(points) < 4:
    cv2.waitKey(1)

cv2.destroyAllWindows()

# Convert points to numpy float32 array
pts1 = np.float32(points)
width = 400
height = 600
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Get the perspective transform and warp the image
M = cv2.getPerspectiveTransform(pts1, pts2)
warped_image = cv2.warpPerspective(image, M, (width, height))

# Display the transformed image
cv2.imshow("Warped Image", warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
