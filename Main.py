# Joshua Williams
# CST 205 T/Th 10-12
# Project 1
# Purpose: Create a new image from a set of 9, and remove extraneous pixels (such as a pedestrian)
# Github link: https://github.com/DrDoctor299/Project-1---CST-205

#Import Pillow

from PIL import Image

#Upload images 
img1 = Image.open("ProjectOneImages/1.png")
img2 = Image.open("ProjectOneImages/2.png")    
img3 = Image.open("ProjectOneImages/3.png")
img4 = Image.open("ProjectOneImages/4.png")
img5 = Image.open("ProjectOneImages/5.png")
img6 = Image.open("ProjectOneImages/6.png")
img7 = Image.open("ProjectOneImages/7.png")
img8 = Image.open("ProjectOneImages/8.png")
img9 = Image.open("ProjectOneImages/9.png")
imgList = [img1,img2,img3,img4,img5,img6,img7,img8,img9]

#Count Length and width
width, height = imgList[1].size

#Create new image (not initialized, so we can fill it in later)
finalImage = Image.new("RGB", (width, height), "red")

#Nested for loops will allow us to iterate through all positions on the images
for y in range(height):    
    for x in range(width):
        
        #Save the current position as a tuple (for ease of use later)
        position = (x,y)
        #Initialize lists to hold values from the red green and blue channels
        redList = []
        greenList = []
        blueList = []
        
        #Iterate through all 9 images at the current position and append each channel value to the end of it's appropriate list
        for i in range(9):
            redValue, greenValue, blueValue = imgList[i].getpixel(position)
            #red channel 
            redList.append(redValue)
            #green channel
            greenList.append(greenValue)
            #blue channel
            blueList.append(blueValue)
        
        #Find median of R G and B
        #Sort each list
        redList.sort()
        greenList.sort()
        blueList.sort()
        #Find the middle value of each list (Lists are known to be odd)
        redValue = redList[((len(redList)+1)/2)]
        greenValue = greenList[((len(greenList)+1)/2)]
        blueValue = blueList[((len(blueList)+1)/2)]
        
        #Add the new color channel values (determined by the median values) to the previously initialized image object
        finalImage.putpixel(position, (redValue, greenValue, blueValue))
        
#Save final image as a png file (Named "final") in the directory that the original images were found in
finalImage.save("Final.png")