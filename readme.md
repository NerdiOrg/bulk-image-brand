# BulkImageBrand
This tool is used to add an image, such as a logo or copyright symbol, on the bottom of every single image in the /images/ directory. It is used for processing these photos in bulk to save editors time and effort.

BulkImageBrand.py Version 0.0.1 was created and submitted to GitHub by William Passmore on 6-26-2019.

## Images Directory
Put your images inside of this directory. The images directory is automatically created on your system if it does not exist already.

## Finished Directory
The finished images will be saved in this directory. Clear out after each use if you believe you may have a naming problem. Files will overwrite by default if the name is taken. The images directory is automatically created on your system if it does not exist already.

## Run.py
Run this script to begin the process. 
1) Type the path to (if applicable, from run.py's working directory) the image you want pasted on the /images/ background images. 
2) Choose new dimensions for the paste image, or type 0 for width & height to maintain the original dimensions.
3) Choose the corner you would like the paste image to appear on.
4) Choose the number of offset pixels you wish the paste image to have as padding from the background image sides.
5) Script will paste the image on to each /images/ background image and save in /finished/ directory.
