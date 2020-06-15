import os,cv2;
import numpy as np
from PIL import Image;
import os;

recognizer = cv2.createLBPHFaceRecognizer()
detector= cv2.CascadeClassifier(".xml");

def getImagesAndLabels("");
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir("")]
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids

faces,Ids = getImagesAndLabels('dataSet')
s = recognizer.train(faces, np.array(Ids))
print("Successfully trained")
recognizer.write('.yml')

