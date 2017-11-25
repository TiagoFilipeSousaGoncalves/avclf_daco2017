import os
import matplotlib.pyplot as plt
import numpy as np
import retinal_image as ri
import apply_skeleton
import find_interestpoints 
import divideIntoSegments
import detectOpticDisk
import apply_homomorphic_filtering
import cv2
from skimage.morphology import skeletonize
from skimage.exposure import rescale_intensity, equalize_adapthist
#import find_interestpointsv2 

#Paths
path_to_training_retinal_ims = 'data/training/images/'
path_to_training_retinal_masks = 'data/training/masks/'
path_to_training_retinal_vessels = 'data/training/vessels/'
path_to_training_arteries = 'data/training/arteries/'
path_to_training_veins = 'data/training/veins/'
path_to_training_inpainting = 'data/training/inpainting/'

retinal_im_list = os.listdir(path_to_training_retinal_ims)

#Open images
for i in range  (len(retinal_im_list) - 1):
    image_object = ri.retinal_image(retinal_im_list[i], 'train')
    
    img_rgb=image_object.image; 
    image_vessels=image_object.vessels
    image_inpainting=image_object.inpainting
    
    
    #Do you want to plot?
    plotFlag=1
    
    # perform skeletonization
    skeleton=apply_skeleton.apply_skeleton(image_vessels,plotFlag)
    
    #Find interest points
    coordinates=find_interestpoints.find_interestpoints(skeleton,plotFlag)
    
    #Divide into segments
    labels = divideIntoSegments.divideIntoSegments(skeleton, coordinates,plotFlag)
    
    #Homomorphic filtering to reduce 
    #img_rgb=apply_homomorphic_filtering.apply_homomorphic_filtering(image_object,image_inpainting,plotFlag)
    #import grey_world
    #img_rgb = grey_world(img_rgb)
    #Detect optic disk
    #img_gray=cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    #contrast stretching 
    img_rgb = rescale_intensity(img_rgb) ## Melhor
   # img_rgb = np.unit8(img_rescale)
   # img_rgb = equalize_adapthist(img_rgb)  ##Tbm é boa
    detectOpticDisk.detectOpticDisk(img_rgb,0)
#
#from skimage.measure import regionprops
#
#regions=regionprops(labels)
#import math
#
#orientations_image=np.zeros((img_rgb.shape[0],img_rgb.shape[1]))
#i=0
#vessel_keypoints=[];
#discretized_lines=[]; 
#discretized_singleline=[]; 
#from skimage.draw import line_aa
#
#diameter=np.zeros(np.max(labels))
#
#for props in regions:
#    i=i+1; 
#    y0, x0 = props.centroid
#    orientation = props.orientation
#    orientations_image[labels==i]=orientation; 
#    x1 = x0 + math.cos(orientation) * 0.5 * props.major_axis_length
#    y1 = y0 - math.sin(orientation) * 0.5 * props.major_axis_length
#  
#    x3 = x0 + math.cos(math.pi/2 + orientation)*0.5*props.major_axis_length;
#    y3 = y0 - math.sin(math.pi/2 + orientation) * 0.5 * props.major_axis_length; 
#    
#    start_x=x0 - math.cos(math.pi/2 + orientation)*0.25*props.major_axis_length;
#    start_y=y0 + math.sin(math.pi/2 + orientation) * 0.25 * props.major_axis_length; 
#    end_x=x0 + math.cos(math.pi/2 + orientation)*0.25*props.major_axis_length;
#    end_y=y0 - math.sin(math.pi/2 + orientation) * 0.25 * props.major_axis_length;
#    tempImg=np.zeros((img_rgb.shape[0],img_rgb.shape[1]))
#
#    rr, cc, val = line_aa(int(start_x), int(start_y), int(end_x), int(end_y))
#    tempImg[cc,rr]=1; 
#    thin_perpendicularlines=skeletonize(tempImg)
#    coordinates=np.nonzero(thin_perpendicularlines)
#   # plt.imshow(skeleton)
#    plt.imshow(image_vessels)
#    plt.plot((start_x, end_x), (start_y, end_y), '-r', linewidth=2.5)
#    plt.scatter(x=rr,y=cc,c='b',s=20,marker='x') 
#    plt.scatter(x=coordinates[1],y=coordinates[0],c='g',s=20,marker='o')
#    plt.show()
#    diameter[i-1]=np.count_nonzero(image_vessels*thin_perpendicularlines) 
#
#    #plt.plot((x0, x1), (y0, y1), '-g', linewidth=2.5)
#   
#    line=np.transpose([i,start_x, start_y, end_x,end_y])
#    vessel_keypoints.append(line)
#    
#np_vesselkeypoints=np.array(vessel_keypoints)
##Organized as follows: label , x0, y0 , x3 , y3. How to discretize ?
#
#
