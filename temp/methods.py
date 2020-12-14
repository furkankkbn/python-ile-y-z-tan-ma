import cv2

import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float,io
from skimage.measure import compare_ssim

print(cv2.__version__)

directory_recognition_face = "./recognitions/"
directory_recognition_classes = "./classess/"

def Find_Face(image_path):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    
    aranan = cv2.imread(directory_recognition_classes+"aranan.png")
    aranan_gray = cv2.cvtColor(aranan,cv2.COLOR_BGR2GRAY)
    aranan = img_as_float(aranan_gray)
    
    for i,(x, y, w, h) in enumerate(faces):
        face_img = image[y:y+h, x:x+w]
        face_file_name = directory_recognition_face + "face_" + str(i) + ".png"
        
       
        face_img = cv2.resize(face_img,(75,75))
        aranan = cv2.resize(aranan,(75,75))
        cv2.imwrite(face_file_name, face_img)
        
        #print("SSIM Skor :",SSIM(aranan,face_img))
        
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
        
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    

def SSIM(aranan,image):
    score = compare_ssim(aranan, image, full=True)
    return score

    
if __name__ == '__main__':
    Find_Face("./resim.png")