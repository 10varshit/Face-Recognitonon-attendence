import pandas as pd
import cv2
import numpy as np
import dateandtime
import os
import face_recognition
import dateandtime
from tkinter import *
import datetime
import time
from PIL import ImageTk, Image
ap=Tk()
ap.geometry('500x350')
ap.config(bg="pink")
ap.title("Binary")
im=Image.open('face.png')
im=im.resize((20,20))
im=ImageTk.PhotoImage(im)
ap.iconphoto(False,im)

def Entry():
    path = 'facesdect'
    imgs = []
    classnames = []
    mylist = os.listdir(path)

    for cl in mylist:
        curimg = cv2.imread(f'{path}/{cl}')
        imgs.append(curimg)
        classnames.append(os.path.splitext(cl)[0])
    print(classnames)
    def encode(imgs):
        encodelst = []
        for img in imgs:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodeimg = face_recognition.face_encodings(img)[0]
            encodelst.append(encodeimg)
        return encodelst

    def markatten(name):
        with open('Entry.csv', 'r+') as f:
            mydatalist = f.readlines()
            namelst = []
            for line in mydatalist:
                entry = line.split(",")
                namelst.append(entry[0])
            if name not in namelst:
                now = datetime.datetime.now()
                days=datetime.datetime.now()
                day=days.strftime("%A")
                dtsrtring = now.strftime('%H:%M:%S')
                f.writelines(f'\nEntry,\nName,Time,Day,\n{name},{dtsrtring},{day}')

    encodelistknown = encode(imgs)
    print("encoding complete")

    statusbar.set("Loading...")
    sbar.update()
    time.sleep(5)
    statusbar.set("Done")

    web = cv2.VideoCapture(0)
    while True:
        flag=0
        success, img = web.read()
        imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
        faceincur = face_recognition.face_locations(imgs)
        encodeimgofcur = face_recognition.face_encodings(imgs, faceincur)

        for encodeFace, faceloc in zip(encodeimgofcur, faceincur):
            matches = face_recognition.compare_faces(encodelistknown, encodeFace)
            faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
            matchindex = np.argmin(faceDis)

            if matches[matchindex]:
                name = classnames[matchindex].upper()
                x1, y1, x2, y2 = faceloc
                x1, y1, x2, y2 = x1 * 4, y1 * 4, x2 * 4, y2 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 1)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 225, 145), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
                markatten(name)
            flag=1
        cv2.imshow('web', img)
        if cv2.waitKey(10) & flag==1:
            break
    web.release()
    cv2.destroyAllWindows()

def Exit():
    path1= 'facesdect'
    imgs1= []
    classnames1= []
    mylist = os.listdir(path1)

    for cl1 in mylist:
        curimg1= cv2.imread(f'{path1}/{cl1}')
        imgs1.append(curimg1)
        classnames1.append(os.path.splitext(cl1)[0])
    print(classnames1)

    def encode(imgs1):
        encodelst1 = []
        for img1 in imgs1:
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            encodeimg1 = face_recognition.face_encodings(img1)[0]
            encodelst1.append(encodeimg1)
        return encodelst1

    def markattenext(name1):
        with open('Exit.csv', 'r+') as f:
            mydatalist1 = f.readlines()
            namelst1 = []
            for line1 in mydatalist1:
                entry = line1.split(",")
                namelst1.append(entry[0])
            if name1  not in namelst1:
                if "Exit" not in "Entry.csv":
                    now = datetime.datetime.now()
                    days1 = datetime.datetime.now()
                    day1 = days1.strftime("%A")
                    dtsrtring1 = now.strftime('%H:%M:%S')
                    f.writelines(f'\nExit,\nName,Time,Day,\n{name1},{dtsrtring1},{day1}')

    encodelistknown1 = encode(imgs1)
    print("encoding complete")

    statusbar.set("Loading...")
    sbar.update()
    time.sleep(5)
    statusbar.set("Done")

    web1 = cv2.VideoCapture(0)
    while True:
        #flag=0
        success1, img1 = web1.read()
        imgs1 = cv2.resize(img1, (0, 0), None, 0.25, 0.25)
        imgs1 = cv2.cvtColor(imgs1, cv2.COLOR_BGR2RGB)
        faceincur1 = face_recognition.face_locations(imgs1)
        encodeimgofcur1 = face_recognition.face_encodings(imgs1, faceincur1)

        for encodeFace1, faceloc1 in zip(encodeimgofcur1, faceincur1):
            matchesxt1= face_recognition.compare_faces(encodelistknown1, encodeFace1)
            faceDis1 = face_recognition.face_distance(encodelistknown1, encodeFace1)
            matchindexext1= np.argmin(faceDis1)

            if matchesxt1[matchindexext1]:
                name1 = classnames1[matchindexext1].upper()
                x1, y1, x2, y2 = faceloc1
                x1, y1, x2, y2 = x1 * 4, y1 * 4, x2 * 4, y2 * 4
                cv2.rectangle(img1, (x1, y1), (x2, y2), (255, 255, 255), 1)
                cv2.rectangle(img1, (x1, y2 - 35), (x2, y2), (0, 225, 145), cv2.FILLED)
                cv2.putText(img1, name1, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
                markattenext(name1)
                #flag=1
        cv2.imshow('web1', img1)
        if cv2.waitKey(10) & 0xff==ord('x'):
            break
    web1.release()
    cv2.destroyAllWindows()
statusbar=StringVar()
statusbar.set("Ready")
sbar=Label(ap,textvariable=statusbar,bg='light blue',height=2,font="Comicsans 12 bold")
sbar.pack(side=BOTTOM,fill=X)

label1=Label(ap,text="Welcome!",bg="light blue",font="Comicsans 30 bold").pack(fill=X)
label2=Label(ap,text="Enter before you proceed",bg="light blue",font="Comicsans 20 bold").pack(fill=X,pady=15)
but1=Button(ap,text="ENTRY",bg="light blue",width=10,height=4,command=Entry).pack(side=LEFT,padx=90)
but2=Button(ap,text="EXIT",bg="light blue",width=10,height=4,command=Exit).pack(side=LEFT,padx=70)
ap.mainloop()
