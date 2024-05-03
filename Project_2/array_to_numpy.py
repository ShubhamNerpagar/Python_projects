import numpy as np
from PIL import Image

data = np.zeros([5, 4, 3])
data[:] = [255, 255, 0]
print(data)


img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
