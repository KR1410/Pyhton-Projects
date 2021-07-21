import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

file_name=f"video_{str(time.strftime('%d-%m-%Y %H-%M-%S'))}.mp4"

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,height))

while True:
    screen_img = ImageGrab.grab(bbox=(0,0,width,height))
    array_img = np.array(screen_img)
    color_img = cv2.cvtColor(array_img,cv2.COLOR_BGR2RGB)

    capture_video.write(color_img)

    cv2.imshow('Screen Recorder', color_img)
    if cv2.waitKey(1) == ord('q'):
        break
