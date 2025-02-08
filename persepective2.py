import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

class PerspectiveTransformer:
    def __init__(self):
        self.image = None
        self.points = []
        self.width = 400
        self.height = 600
        self.clone = None

    def load_image(self):
        self.image = cv2.imread('tennis2.jpeg')
        if self.image is None:
            print("Failed to load image.")
            return False
        
        self.clone = self.image.copy()
        return True

    def draw_point(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Draw a circle at the clicked point
            cv2.circle(self.clone, (x, y), 5, (0, 255, 0), -1)
            self.points.append((x, y))
            cv2.imshow("Image", self.clone)

    def select_points(self):
        if self.image is None:
            print("Load an image first!")
            return None

        self.points = []
        cv2.imshow("Image", self.image)
        cv2.setMouseCallback("Image", self.draw_point)

        print("Click 4 points in this order: Top-left, Top-right, Bottom-left, Bottom-right")
        
        while len(self.points) < 4:
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC key to cancel
                cv2.destroyAllWindows()
                return None

        cv2.destroyAllWindows()
        return self.points

    def transform_perspective(self, points):
        if len(points) != 4:
            print("Need exactly 4 points!")
            return None

        pts1 = np.float32(points)
        pts2 = np.float32([[0, 0], [self.width, 0], 
                           [0, self.height], [self.width, self.height]])

        # Get the perspective transform
        M = cv2.getPerspectiveTransform(pts1, pts2)
        
        # Warp the image
        warped_image = cv2.warpPerspective(self.image, M, (self.width, self.height))
        return warped_image

    def run(self):
        # Load image
        if not self.load_image():
            return

        # Select points
        points = self.select_points()
        if points is None:
            return

        # Transform image
        warped = self.transform_perspective(points)
        
        if warped is not None:
            cv2.imshow("Warped Image", warped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Run the transformer
if __name__ == "__main__":
    transformer = PerspectiveTransformer()
    transformer.run()