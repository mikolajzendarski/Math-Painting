import numpy as np
from PIL import Image

#Crat 3d numpy array of zeros, then replace zeros with yellow pixels

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

#Make a red patch
data[1:3] = [255, 0, 0]
#columns
data[:, 1:3] = [0, 255, 0]
#square
data[1:3, 1:3] = [0, 0, 255]

print(data)
img = Image.fromarray(data, 'RGB')
img.save('canvas.png')


