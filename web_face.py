import cv2,time
face_cascade = cv2.CascadeClassifier("C:\\Users\\admin\\PycharmProjects\\FacePy\\cascade.xml")
vc = cv2.VideoCapture(0)
time.sleep(2)
val,img = vc.read()

cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.25, minNeighbors = 2)
cv2.imshow("Gray",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(faces))
print(faces)
count=0
for x,y,w,h in faces :
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),3)
for i in faces:
    count = count+i

cv2.imshow("Count " + str(count),img)
cv2.waitKey(0)
cv2.destroyAllWindows()



