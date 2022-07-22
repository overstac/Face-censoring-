import cv2

video= cv2.VideoCapture("smile.mp4")
succes, frame= video.read()
height= frame.shape[0]  # 1st dimesiion of the video
width= frame.shape[1]   # 2nd dimesion of the video

face_cascade= cv2.CascadeClassifier("faces.xml")
output= cv2.VideoWriter("blured_smile.avi", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width, height)) #dimesions for video

count=1
while succes:
    faces= face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        frame[y: y+h, x:x+w] = cv2.blur(frame [y+h, x:x+w],(50, 50))
    output.write(frame)
    succes, frame= video.read()
    count+= 1
    print(count)
output.release()