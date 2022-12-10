import skimage
from skimage import io, segmentation

# Load the image
image = io.imread("image.jpg")

# Perform image segmentation
segments = segmentation.slic(image, n_segments=100, compactness=10, sigma=1)

# Display the segmented image
io.imshow(segments)
io.show()
