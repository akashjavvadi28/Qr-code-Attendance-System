import pyqrcode
import png
from pyqrcode import QRCode
import cv2
import webbrowser
import datetime
print("Hi-----------------------------------------------------------------------------------------------------------------")
print("0)To generate a QR for New Student")
print("1)To scan a QR from the Student")
print("-----------------------------------------------------------------------------------------------------------------")
userinput=input("Select a Number: ")

if(userinput=="0"):
  no_of_students=int(input("Enter No.of Students : "))
  for i in range(no_of_students):
    RollNumber=input("Enter Student RollNumber : ").upper()
    url = pyqrcode.create(RollNumber)
    url.png(RollNumber+".png", scale = 6)
    break
elif(userinput=="1"):
  f=open("D:\\EH_Tools\\LIST.csv")
  f.readline()
  students=f.readlines()
  f.close()

  f=open("D:\\EH_Tools\\LIST.csv")
  f.readline()
  students2=f.readlines()
  f.close()

  for i in range(len(students)):
    students[i]=students[i].replace("\n","").upper()
  for i in range(len(students2)):
    students2[i]=students2[i].replace("\n","").upper()
  cap=cv2.VideoCapture(0)
  detector=cv2.QRCodeDetector()
  f=open("D:\\EH_Tools\\Student.csv","a")
  f.write("\n")
  f.write("\n\n")
  f.close()
  while True:
    _,img=cap.read()
    
    data,bbox, _=detector.detectAndDecode(img)
    if(len(data)>1):
        if data in students:
          print(data+"-present")
          now=datetime.datetime.now()
          s=now.strftime("-Present    date: %d-%m-%y    time: %H:%M:%S " )
          status_text = ""
          f=open("D:\\EH_Tools\\Student.csv","a")
          f.write( data+s)
          f.write("\n")
          f.close()
          students.remove(data)
          status_text = f"{data} - Present"
        elif data in students2:
          status_text = f"{data} - Already Present"
        else:
          status_text = "Student is Invalid"
        if bbox is not None:
                for i in range(len(bbox[0])):
                    point1 = tuple(map(int, bbox[0][i]))
                    point2 = tuple(map(int, bbox[0][(i + 1) % len(bbox[0])]))
                    cv2.line(img, point1, point2, (255, 0, 0), 2)
                
                cv2.putText(img, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('show your qr',img)
    if cv2.waitKey(500)==ord('q'):
      break
  print("No.of Students Present: ",len(students2)-len(students))
  print("No.of Students Absent: ",len(students))
  print(students)
  for i in students:
    now=datetime.datetime.now()
    s1=now.strftime("-Absent     date: %d-%m-%y    time: %H:%M:%S " )
    f=open("D:\\EH_Tools\\Student.csv","a")
    f.write(i+s1)
    f.write("\n")
    f.close()


else:
  print("select valid number")
  
  
cv2.destroyAllWindows()
