#code to extract frames from video
import cv2

vidcap = cv2.VideoCapture('1.avi')
success,image = vidcap.read()
count = 0
success = True
print("Converting....")
while success:
  cv2.imwrite("./frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  #print 'Read a new frame: ', success
  count += 1
print("Conversin Done!!!")
