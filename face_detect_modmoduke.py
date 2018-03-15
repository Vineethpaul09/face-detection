from __future__ import print_function
import numpy as np
import cv2
import os
import os.path



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(1)


if os.path.isfile('eye_status.txt'):
        os.remove("eye_status.txt")


 

xrange=0
ramp_frames = 30
 
def get_image():
  retval, im = cap.read()
  return im
  temp = get_image()
print("Taking image...")

camera_capture = get_image()
file = "test_image.png"
file1 = "test_image1.png"

f= open("eye_status.txt","w+")
cnt=0
payload=""
while 1:
        ret, img = cap.read()
        gray = cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectmultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
        
                eyes = eye_cascade.detectmultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    f.write("eyes_open\n")
                    cv2.imwrite(file1, camera_capture)
                   
                    cnt = ab(cnt)- 1
                f.write("eyes_closed\n")
                cnt += 1
                print(cnt)
                
                if cnt > 15:
                        
        
                        try:
                                print("closed eyes vineeth")
                                f.write("eyes_closed\n")
                                delay(1000);
                                cv2.imwrite(file, camera_capture)
                                cnt =0

                        except (KeyboardInterrupt):
                                break

                        except:
                                print ("vinerio")
                if cnt < 5:
                        
                        
                        try:
                                print("open eyes vineeth")
                                f.write("eyes_open\n")

                                
                        except (KeyboardInterrupt):
                                break

                        except:
                                print ("Thing the data.")
                
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
                break

f.close()
cap.release()
cv2.destroyAllWindows()
