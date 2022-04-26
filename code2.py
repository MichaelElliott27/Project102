import cv2
import dropbox
import time
import random

start_time = time.time()

def snapshot():
    number = random.randint(0,50)
    videoCaptureObject = cv2.VideoCapture(0.0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot has been taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def fileType(img_name):
    access_token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file has been uploaded")

def central():
    while(True):
        if ((time.time() - start_time) >= 5.0):
            shot = snapshot()
            fileType(shot)
central()