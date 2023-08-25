import cv2
import os
# import argparse

# argParser = argparse.ArgumentParser()
# argParser.add_argument("-f", "--folder", help="folder path")

# args = argParser.parse_args()

# dir = os.listdir(args.folder)

# for i in range(len(dir)):
#     if i.split(".")[-1] in ['mp4', 'avi']:
#         # Open the input video file

input_path = "55.mp4"
input_video = cv2.VideoCapture(input_path)

# Get the video properties (fps, width, height)
fps = input_video.get(cv2.CAP_PROP_FPS)
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_path = "555.mp4"
output_fps = 10
output_video = cv2.VideoWriter(output_path, fourcc, output_fps, (width, height))

# Read the frames from the input video and write them to the output video
while input_video.isOpened():
    ret, frame = input_video.read()
    if not ret:
        break
    output_video.write(frame)

# Release the video captures and writers
input_video.release()
output_video.release()
