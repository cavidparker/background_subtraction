import cv2
import numpy as np
cap = cv2.VideoCapture('test2.mp4')
fgbg =cv2.createBackgroundSubtractorMOG2()



while True:
	ret, frame = cap.read()
	if frame is None:
		break
	fgmask = fgbg.apply(frame)	

	cv2.imshow('Frame', frame)
	cv2.imshow('FG MASK', fgmask)

	keyboard = cv2.waitKey(30)
	if keyboard == 'q' or keyboard == 27:
		break	


cv2.imshow('cloth_image', cap)

cap.release()
cv2.destroyAllWindows()

