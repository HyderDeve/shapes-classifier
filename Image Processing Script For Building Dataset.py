import cv2
import os

# Create output folder if it doesn't exist
output_folder = 'Id2307BSCS009_shapes'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 1. Load the original image
image = cv2.imread('sample/Pentagons.jpg') # change this path according to the location of the image you want to process
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Thresholding to find the shapes
# We use binary_inv so shapes become white (255) and paper becomes black (0)
# This makes it easier for findContours to work.
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)[1]

# 3. Find Contours
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

image_num = 0
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)

    # Filter out noise (only process items larger than 30x30 pixels)
    if w > 30 and h > 30:
        # A. Crop the original grayscale image
        roi = gray[y:y+h, x:x+w]

        # B. Apply Thresholding to the crop to make it pure black/white
        _, roi_binary = cv2.threshold(roi, 180, 255, cv2.THRESH_BINARY)

        # C. Resize to 28x28
        # We use INTER_AREA which is best for shrinking images
        resized = cv2.resize(roi_binary, (28, 28), interpolation=cv2.INTER_AREA)

        # D. Ensure Black Shape on White Background
        # (If your drawing was black on white paper, roi_binary should already be correct,
        # but this step ensures the background is pure 255 white)

        # E. Save the final 28x28 image
        cv2.imwrite(f'{output_folder}/shape_{image_num}.png', resized)
        image_num += 1

print(f"Finished! Processed {image_num} images into '{output_folder}' folder.")



import shutil
shutil.make_archive(output_folder, 'zip', output_folder)