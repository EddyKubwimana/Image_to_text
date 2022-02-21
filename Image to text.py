import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Kubwi\OneDrive\Desktop\tesseract-ocr-setup-3.02.02.exe'
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.imread('images/mandela-featured-image2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('image', img)
cv2.waitKey(0)