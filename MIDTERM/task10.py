'''
A digital gray-scale image can be stored as a list of lists, 
where each inner list contains the values for one row of the image 
and where each value can take on a number between 0 (pure black) and 255 (pure white). 

Example 1 draws out a picture of the upper case letter "B" in dark gray (value 50) on a white (value 255) background. 
Example 2 shows a white-to-black gradient going from the top left corner to the bottom right corner.

Your task is to implement two functions: 
1. invert, which inverts the colors of an image, 
- Inverting a picture: changing dark values to light values and light values to dark values. 
- In our case, 255 would need to be changed to 0, 254 to 1, 253 to 2 and so on, 
all the way to changing 0 to 255. See Example 3 below for how Example 1 is inverted.

2. and flip_vertical, which flips the picture vertically.
- Flipping a picture vertically: the 1st row of the image (at the top) becomes the last row (at the bottom), 
the second row becomes the second-to-last row, and so on. 
- If there's an un-even number of rows, the middle row stays where it is. 
See Example 4 for the vertically flipped gradient of Example 2.

It is up to you if you want to return the input lists changed in-place 
or to return new lists. Both solutions are valid, just make sure you return the result.
'''
# Example 1: a black-on-white shape that looks like the upper-case letter B
e1 = [
 [ 50, 50,255],
 [ 50,255, 50],
 [ 50, 50,255],
 [ 50,255, 50],
 [ 50, 50,255]]

# Example 2: A white-to-black gradient from top-left to bottom-right
e2 = [
 [255,191,127],
 [191,127, 63],
 [127, 63, 0]]

# Example 3: The B-shape with its colors inverted
e3 = [
 [205,205, 0],
 [205, 0,205],
 [205,205, 0],
 [205, 0,205],
 [205,205, 0]]

# Example 4: The gradient flipped vertically
e4 = [
 [127, 63, 0],
 [191,127, 63],
 [255,191,127]]

# Calling invert with Example 1 as the parameter should return Example 3
def invert(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = 255-img[i][j]
    return img

# Calling flip_vertical with Example 2 as the parameter should return Example 4
def flip_vertical(img):
# my solution
#    lst = []
#    for i in range(len(img)-1,-1,-1):
#        lst.append(img[i])
#    return lst
    img.reverse() # solution
    return img

# print statements for your convenience.
# Note that, of course, these print statements will print your rows
# without line breaks, but that doesn't matter. What matters are the values.
print(e1)
print(invert(e1)) # should look like e3
#print(e3)
print(e2)
print(flip_vertical(e2)) # should look like e4
print(e4)