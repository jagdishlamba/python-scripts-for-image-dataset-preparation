import os
import cv2


folders = ['D:\\trg_yolo7\\yolov7-main\\license_plate_civVeh\\train']


for folder in folders:
	for textfile in os.scandir(folder):
		if textfile.endswith("txt"):
			try:
				with open(textfile, "r") as file:
				    # Read the contents of the file
				    contents = file.read()
				    a = contents.split(" ")
				    a[0] = str(0)
				with open(textfile, "w") as file:
				    # Write the contacts to the file
				    file.write(" ".join(a))
			except:
				continue

print("Done wrk")

