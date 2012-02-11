__author__ = 'dfrysing'

import cv2
import numpy
import time

cv2.namedWindow("My Window")

video = cv2.VideoCapture('P1_4.m4v')

successFlag, frame = video.read()

lastFrame = frame.copy()

h, w = frame.shape[:2]
motionHistory = numpy.zeros((h, w), numpy.float32)

while 1:
    successFlag, frame = video.read()

    if not successFlag:
        break

    frameDiff = cv2.absdiff(lastFrame, frame)
    greyDiff = cv2.cvtColor(frameDiff, code=cv2.COLOR_BGR2GRAY)

    retval, motionMask = cv2.threshold(greyDiff,10,1,cv2.THRESH_BINARY)

    timestamp = time.clock()
    cv2.updateMotionHistory(motionMask, motionHistory, timestamp, 0.5)
    mg_mask, mg_orient = cv2.calcMotionGradient( motionHistory, 0.25, 0.05, apertureSize=5 )
    seg_mask, seg_bounds = cv2.segmentMotion(motionHistory, timestamp, 0.25)

    total = sum(sum(motionHistory))/8
    print "movement: ", total

    cv2.imshow("My Window", motionHistory)
    cv2.waitKey(1)

    lastFrame = frame.copy()
