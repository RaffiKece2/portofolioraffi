import cv2
import cv2.data
from deepface import DeepFace



wadah_umur = ['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60+)']


age_net = cv2.dnn.readNetFromCaffe('deploy_age.prototxt','age_net.caffemodel')


face_casade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



img = cv2.imread("raffi.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_casade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

for x,y,w,h in faces:
    face = img[y:y + h, x:x + w]
    blob = cv2.dnn.blobFromImage(face,1.0,(227,227),(78.4263,87.7689,114.8958),swapRB=False)
    hasil = DeepFace.analyze(face,actions=['emotion'],enforce_detection=False)
    verifikasi = DeepFace.verify(face,"mama.jpg",enforce_detection=False)
    emosi = hasil[0]['dominant_emotion']
    wajah_cocok = verifikasi["verified"]
    age_net.setInput(blob)
    age_prediksi = age_net.forward()
    age = wadah_umur[age_prediksi[0].argmax()]
    
    cv2.rectangle(img,(x,y),(x + w, y + h),(0,255,0),2)
    cv2.putText(img,f"Umur: {age}",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
    cv2.putText(img,f"Emosi:{emosi}",(x,y + 50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.putText(img,f"Verifikasi:{wajah_cocok}",(x,y + 250),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2)
    


cv2.imshow("Umur Prediksi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()