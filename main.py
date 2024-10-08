from stockfish import Stockfish

stockfish = Stockfish("/usr/bin/stockfish")
# print(stockfish.get_board_visual())

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./images/image2.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

edges = cv2.Canny(blurred_image, 50, 150)
plt.imshow(edges, cmap="grey")
# plt.imshow(image_rgb)
plt.axis("off")
plt.show()
# print(image_rgb)
