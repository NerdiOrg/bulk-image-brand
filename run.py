from PIL import Image
import os, glob
curr = "./"
images = curr + "images" # do not include end slash
finished = "finished"
finishdir = curr + finished

def getimg():
    valid = False
    while valid == False:
        print("\nSupply the path/filename for the image.")
        print("The path must be given only from current directory of ./run.py")
        print("Do not include the first / in the path from script root.")
        imginput = input("Please type the exact filename of your image ...Then press ENTER\n")
        imgpath = curr + "/" + imginput
        print("Attempting to find image...")
        if not os.path.exists(imgpath):
            print("\nThe image/path '" + imgpath + "' does not exist. Try again!\n\n")
        else:
            print("Image found!")
            try:
                img = Image.open(imgpath).convert("RGBA")
                print("Successfully opened image & converted to RGBA.")
                valid = True
                imgw, imgh = img.size
                return [img, imgw, imgh]
            except:
                print("There was an error when attempting to open the image or convert to RGBA.")


def checkmakedir(dir): # make dir if it doesn't exist
    if not os.path.exists(dir):
        try:
            os.mkdir(dir)
            return True
        except:
            if not os.path.exists(dir): # still doesn't xist, but couldn't make it
                print("Could not create directory " + dir)
                exit()
            # else: ~~ this would mean the the path already exists / created after first check, before mkdir
            exit()

print("Thank you for using William Passmore's Bulk Image Branding tool in Python!")
checkmakedir(images)
checkmakedir(finishdir)

overlay, overlayw, overlayh = getimg()

validBrandW = False
print("\nHow many pixels should your brand image be in Width? Type 0 to not change source image.")
while validBrandW == False:
    brandW = input("Type in the number of pixels, without 'px':\n")
    if brandW.isdigit():
        try:
            brandW = int(brandW)
            validBrandW = True
        except ValueError:
            brandW = 0
            print("You must enter a valid integer for width, in pixels.\n")

validBrandH = False
print("\nHow many pixels should your brand image be in Height? Type 0 to not change source image.")
while(validBrandH == False):
    brandH = input("Type in the number of pixels, without 'px':\n")
    if brandH.isdigit():
        try:
            brandH = int(brandH)
            validBrandH = True
        except ValueError:
            brandH = 0
            print("You must enter a valid integer for height, in pixels.\n")

if brandW > 0 and brandH > 0:
    try:
        brandH = int(brandH)
        brandW = int(brandW)
        print("Attempting to resize the image...")
        overlay = overlay.resize((brandW,brandH),Image.ANTIALIAS)
        overlayw = brandW
        overlayh = brandH
        print("Successfully resized brand image.")
    except:
        if brandW > 0 or brandH > 0:
            print("There is an issue resizing the source image. Using original dimensions!")
            overlayw, overlayh = overlay.size
        else:
            print("There is an issue with the image")
        exit()


validCorner = False # changes to false if anything bad occurs
while validCorner == False:
    print("Please type the number that corresponds to the corner that your overlay image should appear in:\n1: Top Left\n2: Top Right\n3: Bottom Right\n4: Bottom Left")
    corner = input("Press ENTER when you have typed your number selection.\n")
    if corner.isdigit():
        corner = int(corner)
        if corner >= 1 and corner <= 4:
            validCorner = True
    if validCorner == False:
        print("\nYou must enter a valid number choice for the corner the overlay image should appear in. Try again!\n\n")

validOffset = False
while validOffset == False:
    print("\nPlease type in the integer amount of pixels that should separate the background image and overlay image.\nType 0 if your overlay image already accounts for this.")
    offset = input("Press ENTER after typing a valid integer.\n")
    if offset.isdigit():
        offset = int(offset)
        validOffset = True
        break
    print("\nYou must enter a valid integer for the offset pixels amount. Try again!\n\n")

os.chdir(images + "/")
for file in glob.glob("*.*"):
    bg = Image.open(file)
    bgw, bgh = bg.size
    print(bgw, bgh)
    print(file)
    if((offset+overlayw) > bgw or (offset+overlayh) > bgh):
        print("The file " + file + " is not big enough to support the defined offset pixels & overlay dimensions. Image: "+str(bgw)+"x"+str(bgw)+"px\nThe offset is "+str(offset)+"px\nThe overlay image dimensions are "+str(overlayw)+"x"+str(overlayh)+"px")

    if corner == 1:
        coords = (0+offset, 0+offset)
    elif corner == 2:
        coords = (bgw-offset-overlayw, 0+offset)
    elif corner == 3:
        coords = (bgw-offset-overlayw, bgh-offset-overlayh)
    else:
        coords = (0+offset, bgh-offset-overlayh)

    bg.paste(overlay, coords, overlay)
    bg.save("../" + finished + "/" + file)
