# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:19:24 2017

@author: Tiago Gonçalves
"""
import cv2
import numpy as np

#Average Values along the perpendicular line

#First of all, we need to convert the RGB image into HSV image:
def InterceptHSVWithMaskPerpendicular(img, mask_with_perpendicular_line):
    #Convert img to RGB and HSV
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    
    #Multiply HSV image by mask with perpendicular line where the central pixel is identified
    new_img = hsv_image * mask_with_perpendicular_line
    new_img = new_img[:,:,2]
    
    #Check where pixel value is equal to one:
    index_zeros = np.array(new_img==1)
    
    return new_img, index_zeros
    
#    
#    
#    #Compare index values with values of the original image
#    
#    for r, c in img.shape:
#        std_matrix = np.zeros(r, c)
#        std_matrix.append(np.std(img[r,c]-new_img[r,c]))
#    #Perform average and save it in features
#    #Tenho de ver o código original para fazer isto.