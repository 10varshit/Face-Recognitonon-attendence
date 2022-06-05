import cv2
import numpy as np
import dateandtime
import os
import face_recognition
img1=face_recognition.load_image_file("facesdect/warren10.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img1tst=face_recognition.load_image_file("facesdect/warren.jpg")
img1tst=cv2.cvtColor(img1tst,cv2.COLOR_BGR2RGB)
faceloc=face_recognition.face_locations(img1)[0]
encodeimg=face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(0,225,225),1)

faceloctst=face_recognition.face_locations(img1tst)[0]
encodeimgtst=face_recognition.face_encodings(img1tst)[0]
cv2.rectangle(img1tst,(faceloctst[3],faceloctst[0]),(faceloctst[1],faceloctst[2]),(225,225,0),1)
results=face_recognition.compare_faces([encodeimg],encodeimgtst)
facedis=face_recognition.face_distance([encodeimg],encodeimgtst)
print(results)
print(facedis)
cv2.putText(img1tst,f'{results} {round(facedis[0],2)},',(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,0),1)
cv2.imshow("warren",img1)
cv2.imshow("warren tst",img1tst)
cv2.waitKey(0)