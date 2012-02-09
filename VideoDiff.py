__author__ = 'dfrysing'

import cv2

lastFrame = None

cv2.namedWindow("My Window")

video = cv2.VideoCapture('P1_4.m4v')

while 1:
    successFlag, image = video.read()

    if not successFlag:
        break

    image = cv2.cvtColor(image, code=cv2.COLOR_BGR2GRAY)

    if lastFrame is None:
        lastFrame = image

    diffImage = cv2.absdiff(lastFrame, image)
    retval, bitImage = cv2.threshold(diffImage,10,255,cv2.THRESH_BINARY)

    total = sum(sum(bitImage))/255
    print "movement: ", total

    cv2.imshow("My Window", bitImage)
    cv2.waitKey(1)

    lastFrame = image
