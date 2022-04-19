import cv2
import time
 
kamera = cv2.VideoCapture(0)

##---------------------------------------

#Burası ek olarak fotoğraf da çekiyor
#this place also takes photo

return_value, image = kamera.read()
cv2.imwrite("image.jpg", image)

##---------------------------------------

time.sleep(1)
 
fourrcc = cv2.VideoWriter_fourcc(*'XVID')
videoKayit = cv2.VideoWriter('video.avi', fourrcc, 17.0, (640, 480))


while (kamera.isOpened()):
    ret, bilgisayarKamerasi = kamera.read()
    if ret == True:
        videoKayit.write(bilgisayarKamerasi)
        if cv2.waitKey(1) &  0xFF == ord('x'):
            break
 
kamera.release()
videoKayit.release()
cv2.destroyAllWindows()