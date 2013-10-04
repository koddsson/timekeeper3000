import cv
from datetime import datetime


class WebcamModule:
    """
    Takes a picture using the webcam and saves it.
    """
    def __init__(self, camera_port=0, image_folder='/home/koddsson/pictures'):
        self.camera_port = camera_port
        self.image_folder = image_folder

    """
    Activate the module. This is run for every module.
    """
    def activate(self, **kwargs):
        capture = cv.CaptureFromCAM(self.camera_port)
        img = cv.QueryFrame(capture)
        location = '%s/IMG_%s.jpg' % (self.image_folder, datetime.now())
        print location
        cv.SaveImage(location, img)
