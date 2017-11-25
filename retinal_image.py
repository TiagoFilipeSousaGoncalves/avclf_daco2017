import os
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color, img_as_float

path_to_training_retinal_ims = 'data/training/images/'
path_to_training_retinal_masks = 'data/training/masks/'
path_to_training_retinal_vessels = 'data/training/vessels/'
path_to_training_arteries = 'data/training/arteries/'
path_to_training_veins = 'data/training/veins/'
path_to_training_inpainting = 'data/training/inpainting/'

path_to_test_retinal_ims = 'data/test/images/'
path_to_test_retinal_masks = 'data/test/masks/'
path_to_test_retinal_vessels = 'data/test/vessels/'
path_to_test_arteries = 'data/test/arteries/'
path_to_test_veins = 'data/test/veins/'
#path_to_test_inpainting = 'data/test/inpainting/'

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
            path_inpaint = path_to_training_inpainting
        elif train_or_test == 'test':
            path_im = path_to_test_retinal_ims
            path_mask = path_to_test_retinal_masks
            path_vessels = path_to_test_retinal_vessels
            path_arteries = path_to_test_arteries
            path_veins = path_to_test_veins
        else:
            print('Invalid mode')
            
        self.image = img_as_float(io.imread(path_im+name))
        self.mask = io.imread(path_mask+name[:-4]+'_mask.gif', dtype=bool)
        self.vessels = io.imread(path_vessels+name, dtype=bool) #[:-4]+'.png'
        self.arteries = io.imread(path_arteries+name, dtype=bool) #[:-4]+'.png'
        self.veins = io.imread(path_veins+name, dtype=bool) #[:-4]+'.png'
        self.inpainting = img_as_float(io.imread(path_inpaint+name))
        
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
        
        
        