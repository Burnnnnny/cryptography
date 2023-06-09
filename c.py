import numpy as np
from PIL import Image

img1 = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
img2 = Image.open('flag_7ae18c704272532658c10b5faad06d74.png')

n1 = np.array(img1)*255
n2 = np.array(img2)*255

#our images have a mode of RGB which is assumed to be an 8-bit int
n_image = np.bitwise_xor(n1, n2).astype(np.uint8)
#Convert to PIL image and save
Image.fromarray(n_image).save('n.png')