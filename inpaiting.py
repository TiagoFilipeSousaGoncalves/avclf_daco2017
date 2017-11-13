import os

import matplotlib.pyplot as plt
import numpy as np

from skimage import io
from skimage import img_as_float
from skimage import color




path_to_training_retinal_ims = 'data/training/images/'
path_to_training_retinal_masks = 'data/training/masks/'
path_to_training_retinal_vessels = 'data/training/vessels/'
path_to_training_arteries = 'data/training/arteries/'
path_to_training_veins = 'data/training/veins/'
retinal_im_list = os.listdir(path_to_training_retinal_ims)

def compute_saturation(retinal_image):
    '''
    This function expects a retinal_image object
    1) retinal image 
    2) Field Of View mask 
    3) binary vessel map
    4) binary artery map
    5) binary vein map
    You may want to use (part of) them, or not
    '''
    return color.rgb2hsv(retinal_image.image)[:,:,1]

def compute_red_intensity(retinal_image):
    '''
    This function expects a retinal_image object.
    '''
    return retinal_image.image[:,:,0]


class retinal_image:   
    def __init__(self, name, train_or_test):
        self.name = name
        if train_or_test == 'train':
            path_im = path_to_training_retinal_ims
            path_mask = path_to_training_retinal_masks
            path_vessels = path_to_training_retinal_vessels
            path_arteries = path_to_training_arteries
            path_veins = path_to_training_veins
        elif train_or_test == 'test':
            path_im = path_to_training_retinal_ims
            path_mask = path_to_training_retinal_masks
            path_vessels = path_to_training_retinal_vessels
            path_arteries = path_to_training_arteries
            path_veins = path_to_training_veins
        else:
            print('Invalid mode')
            
        self.image = img_as_float(io.imread(path_im+name))
        self.mask = io.imread(path_mask+name[:-4]+'_mask.gif', dtype=bool)
        self.vessels = io.imread(path_vessels+name, dtype=bool) #[:-4]+'.png'
        self.arteries = io.imread(path_arteries+name, dtype=bool) #[:-4]+'.png'
        self.veins = io.imread(path_veins+name, dtype=bool) #[:-4]+'.png'
        
        # AVAILABLE FEATURES: These are place-holders for features that you may want to compute out of each image
        self.saturation = None
        self.red_intensity = None
        
    # The retinal_image object knows how to compute these features. 
    # It does that by calling to the functions defined in the previous cells    
    def load_saturation(self):
        # this calls an external function. If the attribute has not been initialized above, this will crash.
        self.saturation = compute_saturation(self)
    
    def load_red_intensity(self):
        self.red_intensity = compute_red_intensity(self)  
        
image = retinal_image(retinal_im_list[15], 'train')
io.imshow(image.vessels)
plt.show() 


from skimage.feature import hog
from skimage import data, color, exposure

from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

image=image.vessels
from skimage.morphology import disk

# perform skeletonization
skeleton = skeletonize(image)

##TODO - MOSTRAR SKELETON EM CIMA DA IMAGEM ORIGINAL 
    
    
# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True,
                         subplot_kw={'adjustable': 'box-forced'})

ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()

from scipy.ndimage import binary_hit_or_miss


B1 = np.array([[0, 1, 0], 
                   [1, 1, 1], 
                   [0, 1, 0]])
B2 = np.array([[1, 0, 1], 
                   [0, 1, 0], 
                   [1, 0, 1]])
B3=np.array([[0, 1, 0], 
                 [1, 1, 1], 
                 [0, 0, 0]])

B4=np.array([[1, 0, 1], 
                 [0, 1, 0],
                 [1, 0, 0]])  

B5=np.array([[0, 1, 0], 
                 [1, 1, 0],
                 [0, 1, 0]])

B6=np.array([[1, 0, 0],
                 [0, 1, 0],
                 [1, 0, 1]])

B7=np.array([[0, 0, 0],
                 [1, 1, 1],
                 [0, 1, 0]])

B8=np.array([[0, 0, 1], 
                 [0, 1, 0],
                 [1, 0, 1]])

B9=np.array([[0, 1, 0],
                [0, 1, 1],
                 [0, 1, 0]])

B10=np.array([[1, 0, 1],
                 [0, 1, 0],
                 [0, 0, 1]])
B11=np.array([[1, 0, 1], 
                 [0, 1, 0], 
                 [0, 1, 0]])

B12=np.array([[0, 1, 0], 
                 [1, 1, 0], 
                 [0, 0, 1]])

B13=np.array([[1, 0, 0], 
                 [0, 1, 1], 
                 [1, 0, 0]])

B14=np.array([[0, 0, 1], 
                 [1, 1, 0], 
                 [0, 1, 0]])

B15=np.array([[0, 1, 0], 
                 [0, 1, 0], 
                 [1, 0, 1]])
B16=np.rot90(B14)
B17 = np.rot90(B15)
B18 = np.rot90(B16)

IMhit_mis=(binary_hit_or_miss(skeleton,B1)+binary_hit_or_miss(skeleton,B2)+binary_hit_or_miss(skeleton,B3)+binary_hit_or_miss(skeleton,B4)+binary_hit_or_miss(skeleton,B5)+binary_hit_or_miss(skeleton,B6)+binary_hit_or_miss(skeleton,B7)+binary_hit_or_miss(skeleton,B8)+binary_hit_or_miss(skeleton,B9)+binary_hit_or_miss(skeleton,B10)+binary_hit_or_miss(skeleton,B11)+binary_hit_or_miss(skeleton,B12)+binary_hit_or_miss(skeleton,B13)+binary_hit_or_miss(skeleton,B14)+binary_hit_or_miss(skeleton,B15)+binary_hit_or_miss(skeleton,B16)+binary_hit_or_miss(skeleton,B17)+binary_hit_or_miss(skeleton,B18))

IMhit_mis_bin=IMhit_mis.astype(np.int); 
coordinates=np.nonzero(IMhit_mis_bin)

coordinates=np.nonzero(IMhit_mis_bin)

plt.figure(3)

plt.imshow(skeleton)
plt.scatter(x=coordinates[1],y=coordinates[0],c='r',s=20,marker='x')
plt.show() 
####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# Applie Homomorphic Filtering  to the image

#import scipy

# Read in image
img1 = retinal_image(retinal_im_list[15], 'train')

img= img1.image

plt.figure(4)
plt.imshow(img)
plt.show() 

plt.figure(5)
plt.scatter(x=coordinates[1],y=coordinates[0],c='r',s=20,marker='x')
plt.show()
plt.imshow(img)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import inpaint



mask = img1.vessels
img_gray = color.rgb2gray(img)
# Defect image over the same region in each color channel
mask = mask.astype(np.float)
image_result = inpaint.inpaint_biharmonic(img, mask, multichannel=True)

fig, axes = plt.subplots(ncols=2, nrows=2)
ax = axes.ravel()

ax[0].set_title('Original image')
ax[0].imshow(img)

ax[1].set_title('Mask')
ax[1].imshow(mask, cmap=plt.cm.gray)

ax[2].set_title('Defected image')
ax[2].imshow(img_gray)

ax[3].set_title('Inpainted image')
ax[3].imshow(image_result)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
