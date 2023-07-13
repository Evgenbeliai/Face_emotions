# 1. Подключение библиотек OpenCV +
# 2. Загрузка изображения 
# 3. Предобработка 
# 4. Обнаружение объектов
# 5. Распознование 
# 6. Вывод

#pip install opencv-python


import cv2

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')



while True:
    statys, kadr = video.read()
    gray = cv2.cvtColor(kadr, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 30)

    for (x,y,w,h) in face:
        cv2.rectangle(kadr,(x,y),(x+w, y+h), (0,0,255),2)
        cv2.putText(kadr, "", (x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 7)

    cv2.imshow("Video", kadr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()    