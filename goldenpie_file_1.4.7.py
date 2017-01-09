# -*- coding: utf-8 -*-
#from __future__ import print_function
#from __future__ import
#from __future__ import
#from __future__ import
import matplotlib.pyplot as plt 
import os.path
import numpy as np 

#def kkk():
#    print('no')
def alpha_down(pic2):
    directory = os.path.dirname(os.path.abspath(__file__)) 
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, pic2)
    # Read the image data into an array
    img = plt.imread(filename)
    
    '''Show the image data'''
    # Create figure with 1 subplot
    fig, ax = plt.subplots(1, 1)
    # Show the image data in a subplot
    ax.imshow(img, interpolation='none')
    
    img = plt.imread(filename)
    
    height = len(img)
    width = len(img[0])
    for r in range(155):
        for c in range(width):
            if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
                img[r][c]=[255,0,255] # R + B = magenta