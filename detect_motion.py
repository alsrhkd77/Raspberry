import cv2
import numpy as np


def diffImage(i0, i1, i2):
    diff0 = cv2.absdiff(i0, i1)
    diff1 = cv2.absdiff(i1, i2)
    return cv2.bitwise_and(diff0, diff1)


def getGrayCamImg(cam):
    img = cam.read()[1]
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def updateCameraImage(cam, i):
    img = cam.read()[1]
    i[0] = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img = cam.read()[1]
    i[1] = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cam.read()[1]
    i[2] = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return i
