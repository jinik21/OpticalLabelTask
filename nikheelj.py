import cv2

def rbg2bla(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #blur=cv2.GaussianBlur(gray,(3,3),0)        #NOISE REDUCING OPTIONAL
    return gray
def sobel_create(img,p1,p2,ksize,h,w,borderType):
    #img=cv2.Canny(img,50,150)          # canny image testing better results of sobel cross 
    sobel_obj=cv2.Sobel(img, cv2.CV_64F, p1, p2, ksize=ksize)

    h=int(0.1*h)
    w=int(0.1*w)

    img_sobel=cv2.copyMakeBorder(sobel_obj,h,h,w,w,borderType=borderType)
 
    return img_sobel


img=cv2.imread('./Chess.jpg')
if img is None:
    print('image opening error')
    exit()
    
print(img.shape)
h,w,_=img.shape
print(h,w)

#grayscale
gray=rbg2bla(img)
print(gray)
cv2.imshow('',gray)
cv2.waitKey(0)
#sobel_X
img_sobel_x=sobel_create(gray,p1=1,p2=0,ksize=3,h=h,w=w,borderType=cv2.BORDER_WRAP)
cv2.imshow('',img_sobel_x)
cv2.waitKey(0)

#sobel_Y
img_sobel_y=sobel_create(gray,p1=0,p2=1,ksize=5,h=h,w=w,borderType=cv2.BORDER_WRAP)
cv2.imshow('',img_sobel_y)
cv2.waitKey(0)

#threshold
_, img_threshold= cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('',img_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
