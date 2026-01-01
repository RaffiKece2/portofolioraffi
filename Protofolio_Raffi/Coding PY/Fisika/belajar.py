import cv2
import cv2.data
import mediapipe as mp
import pyautogui
import math
import numpy as np
import time


 
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5)

face_casade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



screen_w,screen_h = pyautogui.size()

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

angle = 0


img_kacamata = cv2.imread("kacamata.png",cv2.IMREAD_UNCHANGED)






def get_filter(frame,overlay,x,y,scale = 1.0):
    overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    
    w, h = overlay.shape[:2]
    
    
    if x + w > frame.shape[1]:
        w = frame.shape[1] - x
        overlay = overlay[:, :w]
    if y + h > frame.shape[0]:
        h = frame.shape[0] - y
        overlay = overlay[:h]
    
    
    if overlay.shape[2] == 4:
        
        bgr = overlay[:, :, 3]
    
        alpha = overlay[:, :, :3] / 255.0
        
        alpha = np.dstack((alpha,alpha,alpha))
        
        
        roi = frame[y: y + h, x: x  +w ]
        
        blended = (alpha * bgr + (1 - alpha) * roi).astype(np.uint8)
        
        frame[y:y + h, x: x + w] = blended
            
    
    return frame



last_x,last_y = None,None


rect = [100,100,300,300]
rect_a = [50,50,100,100]



box_size = 50


satus_klik = False

hidrogen_klik = False

logo = cv2.imread("logo_a.png")
logo = cv2.resize(logo,(100,100))

sudut_z = 0

while cam.isOpened():
    ret,frame = cam.read()
    
    if not ret:
        break
    
    frame = cv2.flip(frame,1)
    frame_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_casade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    
    result = hands.process(frame_color)
    
    telunjuk_kanan_x = ibu_kanan_x = None
    telunjuk_kanan_y = ibu_kanan_y = None
    telunjuk_kiri_x = ibu_kiri_x = None
    telunjuk_kiri_y = ibu_kiri_y = None
    tengah_kiri_x = tengah_kiri_y = None
    tengah_kanan_x = tengah_kanan_y = None
    
    telunjuk_x = telunjuk_y = None
    ibu_x = ibu_y = None
    
    
    prev_close = False
    toggle = False
    
    
    
    if result.multi_hand_landmarks and result.multi_handedness:
        for idx,hand_landmarks in enumerate(result.multi_hand_landmarks):
            Label = result.multi_handedness[idx].classification[0].label
            
            h,w,_ = frame.shape
     

            
            jari_ibu = hand_landmarks.landmark[4]
            sendi_ibu = hand_landmarks.landmark[3]
            jari_telunjuk = hand_landmarks.landmark[8]
            sendi_telunjuk = hand_landmarks.landmark[7]
            jari_tengah =  hand_landmarks.landmark[12]
            jari_kelingking = hand_landmarks.landmark[16]
            jari_manis = hand_landmarks.landmark[20]
            sendi_tengah = hand_landmarks.landmark[10]
            sendi_tengah_a = hand_landmarks.landmark[9]
            tangan = hand_landmarks.landmark[0]
              

            x1,y1 = int(jari_ibu.x * w),int(jari_ibu.y * h)     
            x2,y2 = int(jari_telunjuk.x * w), int(jari_telunjuk.y * h)
            dx,dy = int(sendi_telunjuk.x * w),int(sendi_telunjuk.y * h)
            x3,y3 = int(jari_tengah.x * w), int(jari_tengah.y * h)
            x4,y4 = int(sendi_tengah.x * w),int(sendi_tengah.y * h)
            x5,y5 = int(sendi_ibu.x * w),int(sendi_ibu.y * h)
            hand_x,hand_y = int(tangan.x * w), int(tangan.y * h)
            x6,y6 = int(jari_kelingking.x * w), int(jari_kelingking.y * h)
            x7,y7 = int(jari_manis.x * w), int(jari_manis.y * h)
            tengah_x ,tengah_y = int(sendi_tengah_a.x * w),int(sendi_tengah_a.y * h)
            
            
            
            if Label == "Right":
                telunjuk_kanan_x = x2
                telunjuk_kanan_y = y2
                ibu_kanan_x = x1
                ibu_kanan_y = y1
                tengah_kanan_x = x3
                tengah_kanan_y = y3
            elif Label == "Left":
                telunjuk_kiri_x = x2
                telunjuk_kiri_y = y2
                ibu_kiri_x = x1
                ibu_kiri_y = y1
                tengah_kiri_x = x3
                tengah_kiri_y = y3
            
            telunjuk_x = x2
            telunjuk_y = y2
            
            ibu_x = x1
            ibu_y = y1
            
            
            #top_left_x = x2 - logo_w // 2
            #top_left_y = y2 - logo_h // 2
            
            
            box_width = rect[0] - 70 - rect[2] + 70
            box_height = rect[3] -  70 -  rect[1] + 70
            
            box_width_a = rect_a[2] - 70 - rect_a[0] + 70
            box_height_a = rect_a[3] - 70 - rect_a[1] + 70
            
            offset = 350
            
            top_left = (w // 2 - box_width // 2 + offset ,h // 2 - box_height  // 2)
        
            bottom_right = (top_left[0] + box_width ,top_left[1]  +  box_height )
            
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2
            
            top_left_a = (w //2 - box_width_a // 2 + offset, h // 2 - box_height_a // 2 - 200)
            bottom_right_a = (top_left_a[0] + box_width_a,top_left_a[1] + box_height_a)
            
            center_x_a = (top_left_a[0] + bottom_right_a[0]) // 2
            center_y_a = (top_left_a[1] + bottom_right_a[1]) // 2        
        
                
            pos_telunjuk_x = int(jari_telunjuk.x * screen_w)
            pos_telunjuk_y = int(jari_telunjuk.y * screen_h)
            
            pos_ibu_x = int(jari_ibu.x * screen_w)
            pos_ibu_y = int(jari_ibu.y * screen_h)
            
        
            
            
            
            
            jarak = math.hypot(x2 - center_x, y2 - center_y)
            
            
            cv2.line(frame,(x2,y2),(center_x,center_y),(0,255,0),3)
            
            cv2.putText(frame,f"Jarak: {int(jarak)}",(x2,y2 - 10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            
            
            if jarak < 90 and not satus_klik:
                satus_klik = True
            else:
                satus_klik = False
            
            
            
            
            
            
            
    h,w,_ = frame.shape 
    box_width = rect[0] - 70 - rect[2] + 70
    box_height = rect[3] -  70 -  rect[1] + 70               
    offset = 350
            
    top_left = (w // 2 - box_width // 2 + offset ,h // 2 - box_height  // 2)
        
    bottom_right = (top_left[0] + box_width ,top_left[1]  +  box_height )
        
    cv2.rectangle(frame,top_left,bottom_right,(0,255,0),2)
    
    for x,y,w,h in faces:
        
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        
        if satus_klik:
                
            filter_w = w
                
            filter_h = int(img_kacamata.shape[0] * (w / img_kacamata.shape[1]))
                
            x_offset = x
            y_offset = y + int(h / 4)
                
            frame = get_filter(frame,img_kacamata,x_offset,y_offset,scale= filter_w / img_kacamata.shape[1])

            
            
            
            
            
                    
        
     
    

                           
    
    cv2.imshow("HandTracking",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

cam.release()
cv2.destroyAllWindows()