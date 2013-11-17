#!/usr/bin/python

import numpy as np
import Image
import random

imagewidth = 100

imgsrc = [random.randint(0,255) for i in xrange(3 * imagewidth**2)]
img_data = np.array(imgsrc, dtype=np.uint8).reshape((imagewidth,imagewidth,3))

img = Image.fromarray(img_data)
img.save('./random.png')
