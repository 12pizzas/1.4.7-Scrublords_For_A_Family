#Josh Lyman 1.4.7 CSP Per. 7
from __future__ import print_function
import PIL
import matplotlib.pyplot as plt
import os.path
import numpy as np

#Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))
cow_file = os.path.join(directory, 'cow.jpg')

#Show the new image in a new window
cow_img = PIL.Image.open(cow_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(cow_img, interpolation='none')
fig.show()










def Mist(original_image, transparency):
    '''Makes the image more transparent
    
    Take the second image that will be displayed on the first image
    and lowers the alpha channel or opaqueness.
    Will paste the image onto the First Image in a certain position.'''
    #Open and show the new image in a new window
    cow_img = PIL.Image.open(cow_file)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(cow_img, interpolation='none')
    
    