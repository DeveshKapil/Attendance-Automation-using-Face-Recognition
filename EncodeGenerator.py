import face_recognition
import pickle
import os
import cv2
import firebase_admin
from firebase_admin import credentials
from PIL import Image

from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://face-recognition-mp1-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-mp1.appspot.com"
})



folderPath = 'Image'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    test_img = cv2.resize(cv2.imread(os.path.join(folderPath, path)), (215, 215))
    imgList.append(test_img)
    studentIds.append(os.path.splitext(path)[0])
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)



print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")