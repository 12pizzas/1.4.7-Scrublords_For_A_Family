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
    Will paste the image onto the First Image in a certain position.'''
    
    #Open the files in the same directory as the Python script
    directory = os.path.dirname(os.path.abspath(__file__))
    img2_file = os.path.join(directory, 'mrclean.png')

    #Show the new image in a new window
    img2_img = PIL.Image.open(img2_file)
    fig, ax = plt.subplots(1, 1)
    ax.imshow(img2_img, interpolation='none')
    fig.show()