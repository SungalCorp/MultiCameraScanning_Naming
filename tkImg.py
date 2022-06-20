from telnetlib import IP
import cv2
import json
import time

IMG_PATH = 'IMG/'
CAMERA_IP_PATH = 'CameraIP/IP.json'


with open(CAMERA_IP_PATH) as IP_file:   
        data = json.load(IP_file)

for item in data["Cameras"]:
    print (item["IP"])

    IP = item["IP"]
    ID = item["cameraID"]

    cap = cv2.VideoCapture(IP)

    t = int(time.time())

    ret, frame = cap.read()
    
    imgname = str(ID) + '_' + str(t) + '.jpg'

    cv2.imwrite(IMG_PATH+ imgname, frame)

    # cv2.imshow('frame', frame)

    cap.release()

cv2.destroyAllWindows()   



# traverse the json file find camera IP one by one
# name and take the image
# wirte images to a folder
