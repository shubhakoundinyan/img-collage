import sys
from PIL import Image
import os
import glob
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL
import math
"""
This program creates a canvas of all the photos uploaded to Desktop by the user
"""
c="d"

print ("Please upload all your photos to Desktop")
	
	
path = "C:\Users\Shubha\Desktop"

im1 = []


for filename in glob.glob(os.path.join(path, '[!test]*.jpg')):
	#if not filename.startswith('test'):
	im1.append(filename)
	#else:
	#	continue

print "IM1:\n"
print im1		

images = map(Image.open, im1)


widths, heights = zip(*(i.size for i in images))
w =(max(widths))
h = (max(heights))
w1 = min(widths)
h1 = min(heights)
mw = math.floor((w+w1)/2)
mh = math.floor((h+h1)/2)
print "Mean Ht:"+str(mh)+"Mean wth:"+str(mw)
total_width = w * len(im1)
#total_width = sum(widths) 
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

for item in im1: 
	path1 = "C:\Users\Shubha\Desktop\Save"
	head , tail = os.path.split(item)
	
	img = Image.open(item)
	#wpercent = (basewidth / float(img.size[0]))
	#hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((w, h), PIL.Image.ANTIALIAS)
	
	img.save(path1 + tail)

im2 = []	
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'Save' in i:
		if not i.startswith('Savetest'):
			im2.append(i)
		else:
			break
print "IM2:"
print im2	

images1 = map(Image.open, im2)
x_offset = 0
for im in images1:
  new_im.paste(im, (x_offset,0))
  
  x_offset += im.size[0]

new_im.save('test.jpg')
#imgplot = plt.imshow(new_im)
#plt.show()

#Delete resized files

for file in os.listdir(path):
    if os.path.isfile(file) and file.startswith("Save"):
         try:
              os.remove(file)
         except Exception,e:
              print e
"""
for fname in os.listdir(path):
    if fname.startswith("Save"):
        os.remove(os.path.join(path, fname))
		
"""