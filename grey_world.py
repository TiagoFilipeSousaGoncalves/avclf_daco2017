

from skimage import img_as_float
import numpy as np

def grey_world(image):
    image = img_as_float(image)
    mu_g = np.average(image[:,:,1])
    image[:,:,0] = np.minimun (image[:,:,0]*(mu_g/np.average(image[:,:,0])),1)
    image[:,:,2] = np.minimun (image[:,:,2]*(mu_g/np.average(image[:,:,2])),1)
    return image