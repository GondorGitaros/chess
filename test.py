import cv2
import numpy as np

# Load the image
img = cv2.imread('screenshot.png')

# Define the RGB value for the arrow
arrow_color = np.array([138, 114, 107])

# Define a small threshold for color variation
threshold = np.array([15, 15, 15])

# Create a mask for pixels within the threshold of the arrow color
mask = cv2.inRange(img, arrow_color - threshold, arrow_color + threshold)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Check if any contours were found
if contours:
    # Assuming the arrow contour is the largest by area
    arrow_contour = max(contours, key=cv2.contourArea)

    # Draw bounding box around the arrow
    x, y, w, h = cv2.boundingRect(arrow_contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Find centroid of the arrow
    M = cv2.moments(arrow_contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # Find tip of the arrow as the point farthest from the centroid
    distances = np.sqrt((arrow_contour[:,:,0] - cX)**2 + (arrow_contour[:,:,1] - cY)**2)
    tip_index = np.argmax(distances)
    tip = tuple(arrow_contour[tip_index][0])

    # Divide the chessboard into 64 squares
    square_size = img.shape[0] // 8  # Assuming the chessboard is square

    # Determine which square the tip of the arrow is in
    square_x = tip[0] // square_size
    square_y = tip[1] // square_size

    print(f"The arrow is pointing to square ({square_x}, {square_y})")

    # Display the image with the bounding box
    cv2.imshow('Image with bounding box', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No contours found")