import cv2
from matplotlib import pyplot as plt

image = cv2.imread('17599.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("Image shape:", 17599.jpg.shape)

plt.imshow(image_rgb)
plt.title("My picture")
plt.axis('off')
plt.show()