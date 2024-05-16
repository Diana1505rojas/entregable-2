import cv2 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

celula = r"C:\Users\Sofia Rojas\Desktop\entregable2\celula.jpg"
imagen = cv2.imread(celula)
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
ub,img=cv.threshold(gris,0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
kernel = np.ones((6,6), np.uint8)
dilatada = cv.dilate(img, kernel, iterations = 1)
erosion = cv.erode(dilatada,kernel,iterations = 9) 


total,mask = cv.connectedComponents(erosion)
print("Número de células encontradas:", total)




 



