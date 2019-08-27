import requests
import json
import os
import cv2
IMAGE_TMP='/tmp/test.jpg'

def envioimg(image):
    url = 'https://pydoc.com.br/facedetect/SearchFaceStudyView/?apikey=bee560126e09153f3aa9daba8b84a9e7'
    files = {'conparison': open(image, 'rb').read()}
    data={'key':'a6f3e2679ce82c866924a55585ce8c1f'}
    return requests.post(url, files=files, data=data).text

camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(IMAGE_TMP,gray)
    break
camera.release()
cv2.destroyAllWindows()
ret=json.loads(envioimg(IMAGE_TMP))
os.remove(IMAGE_TMP)

if (ret['completed'] == 'True'):
	uuid=ret['uuid'].lower()
	print(uuid)


