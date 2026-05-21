#! python3
# Import modules and write comments to describe this program.
    
import os
from PIL import Image


for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
    # Check if file extension isn't .png or .jpg.
        if not filename.lower().endswith(".png") and not filename.lower().endswith( ".jpg"):
            numNonPhotoFiles += 1
            continue # skip to next filename
            # Open image file using Pillow.
        try:
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size
            if width > 500 and height > 500:
                numPhotoFiles += 1
            else:
                numNonPhotoFiles += 1
        except:
            numNonPhotoFiles += 1
                # If more than half of files were photos,
                # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(numPhotoFiles, 'photo files in', foldername)