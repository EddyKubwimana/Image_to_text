import cv2
import numpy
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Kubwi\OneDrive\Desktop\tesseract-ocr-setup-3.02.02.exe'
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.imread('images/mandela-featured-image2.png')
#feed=cv2.VideoCapture(0)
#feed.set(3,670)
#feed.set(4,500)
# while True:
# _,img=feed.read

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img =cv2.resize(img,(1000,700))
print(pytesseract.image_to_string(img))
cv2.imshow('image', img,)
cv2.waitKey(0)