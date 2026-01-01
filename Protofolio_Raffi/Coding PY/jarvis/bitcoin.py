import cv2
import cv2.data
import numpy as np



face_casade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


background = cv2.imread("raffi.jpg")

filter_gambar = cv2.imread("kacamata.png",cv2.IMREAD_UNCHANGED)



def get_filter(background,overlay,x,y,scale = 1.0):
    overlay = cv2.resize(overlay,(0,0),fx= scale,fy=scale)
    
    h, w  = overlay.shape[:2]
    
    if x + w > background.shape[1]:
        w = background.shape[1] - x
        
        overlay = overlay[:, : w]
    
    if y + h > background.shape[0]:
        h = background.shape[0] - y
        
        overlay = overlay[:h]
    
    
    if overlay.shape[2] == 4:
        alpha = overlay[:, : , 3] / 255.0
        
        for c in range(3):
            background[y:y + h, x: x + w,c] = (
                
                (1 - alpha) * background[y:y + h, x: x + w, c] + alpha * overlay[:, :, c]
                
            
            )
    
    return background



gray = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
face = face_casade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)


for (x,y,w,h) in face:
    
    filter_w = w

    filter_h = int(filter_gambar.shape[0] * (w / filter_gambar.shape[1]))
    
    x_offset = x
    y_offset = y + int(h / 4)
    
    
    background = get_filter(background,filter_gambar,x_offset,y_offset,scale= filter_w / filter_gambar.shape[1])
    
    

cv2.imshow("COba",background)
cv2.waitKey(0)
cv2.destroyAllWindows()
