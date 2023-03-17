import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        # 3d array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # change zeros with user given color
        self.data[:] = self.color
    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
