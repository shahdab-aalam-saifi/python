# with open("python.png", "rb") as h:
#     with open("new.png", "wb") as n:
#         n.write(h.read())

import numpy as np
import matplotlib.image as mimg

img = mimg.imread("python.png")
mimg.imsave("new.png", np.dot(img[...,:3], [0.2989, 0.5870, 0.1140]))
