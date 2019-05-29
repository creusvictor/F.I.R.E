import os
import pygame
import pygame.camera
import cv2
import numpy as np
from pygame.locals import *

DEVICE = '/dev/video0'
SIZE = (640, 480)
FILENAME = 'capture.png'
class WebCam():
    def __init__(self):
        pygame.init()
        pygame.camera.init()
        self.display = pygame.display.set_mode((640,640), 0)
        self.camera = pygame.camera.Camera(DEVICE, SIZE)

    def start(self):
        self.camera.start()

    def stop(self):
        self.caemra.stop()

    def takeImage(self):
        #pygame.init()
        #pygame.camera.init()
        #display = pygame.display.set_mode(SIZE, 0)
        #camera = pygame.camera.Camera(DEVICE, SIZE)
        screen = pygame.surface.Surface(SIZE, 0, self.display)
        img =  self.camera.get_image(screen)
        return img

    def darknet(self):
        # take picture fro mwebcam
        img_src = self.takeImage()
        # darknet/data
        # ./darknet detect cfg/yolov3.cfg yolov3.weights data/testCam.jpg
        # save img on /testlab
        pygame.image.save(img_src, "testCam.jpg")
        # move image to /darknet/data
        os.system('mv testCam.jpg data')
        # execute darknet with that image
        os.system('./darknet detect cfg/yolov3.cfg yolov3.weights data/testCam.jpg')
        # read the image predictions.jpg
        img_result = pygame.image.load('predictions.jpg')
        # show the result image into interface
        return img_result
        
    def isFire(self):
        video = cv2.VideoCapture(0)
        while True:
            (grabbed, frame) = video.read()
            if not grabbed:
                break
        blur = cv2.GaussianBlur(frame, (21,21), 0)
        hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        
        lower = [18, 50, 50]
        upper = [35, 255, 255]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        
        output = cv2.bitwise_and(frame, hsv, mask=mask)
        no_red = cv2.countNonZero(mask)
        
        if int(no_red) > 15000:
            return True
        else:
            return False

        
