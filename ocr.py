import pytesseract
from PIL import Image
import cv2

ret, frame = cap.read()

if ret:
  gray_frame = cv2.cvColor(frame, cv2.COLOR_BGR2GRAY)

  cropped_frame = gray_frame[0:100, 0:100]

  text = pytesseract.image_to_string(cropped_frame)
  print('extracted text:', text)

  cv2.imshow('cropped frame', cropped_frame)