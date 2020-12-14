import mysql.connector
import base64
import io
import cv2
#import Image
from array import array
from PIL import Image
import numpy as np

"""with open('lemonyellow_logo.jpg', 'rb') as f:
    photo = f.read()
encodestring = base64.b64encode(photo)"""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()

def new_db():
    print("Database işlemleri.")
    #mycursor.execute("CREATE DATABASE FaceDB")
    """mycursor.execute("DROP TABLE FaceDB.Persons")
    mycursor.execute("DROP TABLE FaceDB.Faces")
    mycursor.execute("DROP TABLE FaceDB.Inspection")
    mycursor.execute("CREATE TABLE FaceDB.Persons (person_no VARCHAR(255), name VARCHAR(255), department VARCHAR(255), img_face LONGBLOB NOT NULL,class VARCHAR(50))")
    mycursor.execute("CREATE TABLE FaceDB.Faces (file_name VARCHAR(255), img_face LONGBLOB NOT NULL)")
    mycursor.execute("CREATE TABLE FaceDB.Inspection (date_time VARCHAR(100),person_no VARCHAR(255), name VARCHAR(255), department VARCHAR(255), img_face LONGBLOB NOT NULL,class VARCHAR(50))")
    """
    mycursor.execute("delete from FaceDB.Persons")
    mycursor.execute("delete from FaceDB.Faces")
    mycursor.execute("delete from FaceDB.Inspection")

def insert(person_no,name,department,img,cls):
    #mycursor = mydb.cursor()
    sql = "INSERT INTO FaceDB.Persons (person_no,name,department,img_face,class) VALUES (%s, %s, %s, %s, %s)"
    blob_img = img #base64.b64encode(img)
    val = (person_no,name,department,blob_img,cls)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "inserted.")
    
def insert_faces(file,img):
    sql = "INSERT INTO FaceDB.Faces (file_name,img_face) VALUES (%s,%s)"
    blob_img = img
    val = (file,blob_img)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "inserted.")

def delete_faces():
    sql = "DELETE FROM FaceDB.Faces"
    mycursor.execute(sql)
    mydb.commit()
    
  
def select():
    #mycursor = mydb.cursor()
    data_list = []

    sql ="select * from FaceDB.Persons"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    
    for i,row in enumerate(data):    
        data_value = []
        for j,value in enumerate(row):
            data_value.append(value)
            
        data_list.append(data_value)
    return data_list

def select_faces():
    data_list = []
    sql ="select * from FaceDB.Faces"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    
    for i,row in enumerate(data):    
        data_value = []
        for j,value in enumerate(row):
            data_value.append(value)
        data_list.append(data_value)
    return data_list


def get_Image(data,count):
    file_like=io.BytesIO(data)
    img=Image.open(file_like)
    #img.load()
    W,H=img.size
    """img = np.asarray(img)
    img = cv2.resize(img, (W, H))"""
    #img = np.asarray(img, dtype="int32")
    return img

def read_file(filename):
    img = cv2.imread(filename)
    img = CLAHE(img)
    cv2.imwrite(filename,img)
    
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


def CLAHE(img):
    #img = color.rgb2gray(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    img = cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img = clahe.apply(img[0])
    return img