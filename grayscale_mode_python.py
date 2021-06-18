import cv2

cap = cv2.VideoCapture('video.mp4') # for webcam: cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Grayscale', gray)

cap.release()
cv2.destroyAllWindows()
