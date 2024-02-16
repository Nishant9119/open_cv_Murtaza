import numpy as np
import cv2
#Chapter1
'''
#Recording video
cap = cv2.VideoCapture(0)
#width
cap.set(3,5)
#height
cap.set(4,5)
#brightness
cap.set(10,1002)

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord("x"):
        break
cv2.destroyAllWindows()
'''
#Chapter 2
'''
#Important Functions in cv2
img = cv2.imread("C:/Users/Nikhil Sharma/Pictures/Screenshots/Screenshot 2023-09-23 193915.png")
#grey Image
grey_img = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
#Blurr Image
blurr_img =cv2.GaussianBlur(img,(699,699),0)
#Edge Detector
img_Canny = cv2.Canny(img,75,112)
#Increase Thickness of Edge-Image Dialation
kernel = np.ones((5,5),np.uint8)
img_dialation = cv2.dilate(img_Canny,kernel,iterations=1)
#Eroded Image
img_eroded = cv2.erode(img_dialation,kernel,iterations=2)'''
#Chapter3
'''
#Image Resizing
img = cv2.imread("C:/Users/Nikhil Sharma/Pictures/Screenshots/Screenshot 2023-09-23 193915.png")

img_resize = cv2.resize(img,(2000,2000))
#Cropping Image
img_cropped = img[100:500,300:400]
img11 = cv2.putText(img,text = "Hello",color=(0,0,255),fontFace=cv2.FONT_HERSHEY_SIMPLEX,org = (150,100),fontScale=2)
#img11 = cv2.line(img,pt1 = (100,100) ,pt2 = (400,400) ,color = (0,0,255),thickness = 5)
'''
#cHAPTER 4
'''
#Warp Persepective
img = cv2.imread("C:/Users/Nikhil Sharma/Pictures/Screenshots/Screenshot 2023-09-23 193915.png")

width,height = 250,250 #Final height and width you want
points1 = np.float32([[530,429],[643,429],[534,553],[656,560]]) #Points/coordinates you want warp perspective of
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #Coordinates/size/shape of final image you want
matrix = cv2.getPerspectiveTransform(points1,points2)
image_output = cv2.warpPerspective(img,matrix,(width,height))
print(image_output)
'''
#Color Detection
'''
img = cv2.imread("C:/Users/Nikhil Sharma/Pictures/Screenshots/Screenshot 2023-11-20 203148.png")
img_resized = cv2.resize(img,(500,500))
img_hsv = cv2.cvtColor(img_resized,cv2.COLOR_BGR2HSV)
cv2.namedWindow(winname="trackbars")
cv2.resizeWindow("trackbars",640,240)
def func1(a):
    pass
cv2.createTrackbar("Hue Min","trackbars",0,179,func1)
cv2.createTrackbar("Hue Max","trackbars",179,179,func1)
cv2.createTrackbar("Sat Min","trackbars",0,255,func1)
cv2.createTrackbar("Sat Max","trackbars",255,255,func1)
cv2.createTrackbar("Val Min","trackbars",0,255,func1)
cv2.createTrackbar("Val Max","trackbars",255,255,func1)

#Reading trackbar values
while True:
    img = cv2.imread("C:/Users/Nikhil Sharma/Pictures/Screenshots/Screenshot 2023-11-20 203148.png")
    img_resized = cv2.resize(img, (500, 500))
    img_hsv = cv2.cvtColor (img_resized, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv,lower,upper)
    img_result = cv2.bitwise_and(img_resized,img_resized,mask = mask)
    cv2.imshow("original",img_resized)
    cv2.imshow("image",img_hsv)
    cv2.imshow("masked",mask)
    cv2.imshow("result",img_result)
    cv2.waitKey(1)
'''
#Shapes Detection
def get_contours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area  = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img,cnt,-1,(255,0,0))
img = cv2.imshow("contours_dwtec.jpg")
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blurr = cv2.GaussianBlur(img_grey,(7,7),1)
img_canny = cv2.Canny(img_blurr,60,60)
get_contours(img_canny)
img_blank = np.zeros_like(img)
cv2.imshow("window",img)
cv2.waitKey(0)
