#Josh Lyman 1.4.7 CSP Per. 7
from __future__ import print_function
import PIL
import matplotlib.pyplot as plt
import os.path
import numpy as np


def paste_img2():
    '''Pastes img2 onto top right of img1
    
    Take the second image that will be displayed on the first image
    and lowers the alpha channel or opaqueness.
    Will paste the image onto the First Image at the top right.'''
    
    #Open the files in the same directory as the Python script
    directory = os.path.dirname(os.path.abspath(__file__))
    
    #Define Images
    img1_file = os.path.join(directory, 'cow2.png')
    img1_img = PIL.Image.open(img1_file)
    img2_file = os.path.join(directory, 'mrclean.png')
    img2_img = PIL.Image.open(img2_file)
    img2_small = img2_img.resize((200,200))
    img1_small = img1_img.resize((200,200))
    fig, ax = plt.subplots(1, 1)
    
    #Paste image 2 on image 1
    img2_img.paste(img1_small, (550,25), mask=img1_small)
    ax.imshow(img2_img, interpolation='none')
    
    fig.show()