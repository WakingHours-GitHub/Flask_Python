import time
import numpy as np
import cv2 as cv
from base_camera import BaseCamera

class Camera(BaseCamera):

    def __init__(self):
        super(Camera, self).__init__()



    @staticmethod
    def frames(): # 重写BaseCamera的frames类
        cap = cv.VideoCapture(0)

        if not cap.isOpened():
            return RuntimeError("could nto opened camera.")
        while True:
            res, frame = cap.read()
            # frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            if res:
                yield cv.imencode('.jpg', np.hstack([frame]))[1].tobytes() # to bytes.
            else:
                print("not get cap, please check you camera is opened!")





