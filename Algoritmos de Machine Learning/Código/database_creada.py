import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as img
from skimage import io
from PIL import Image
import cv2
import os
def conversor(imagen):
    col = Image.open(imagen)
    bw = col.convert('L')
    bw.save("bw_image.jpg") 
    img_array = cv2.imread("bw_image.jpg", cv2.IMREAD_GRAYSCALE)
    img_array = cv2.bitwise_not(img_array)
    img_size=28
    new_array = cv2.resize(img_array, (img_size,img_size)) 
    final_array = []
    for lista in new_array:
        for numero in lista:
            final_array.append(float(numero))
    final_array = np.array(final_array) 
    final_array= final_array.reshape(1, -1)
    return(final_array)
base_de_datos_ferra = []
for i in range (62):
    path = os.path.join("Base de datos propia", "Ferrá", f"numero_{i}.png")
    matriz = conversor(path)
    base_de_datos_ferra.append(matriz)
base_de_datos_vicente = []
for i in range (62):
    path = os.path.join("Base de datos propia", "Vicente", f"{i}.PNG")
    matriz = conversor(path)
    base_de_datos_vicente.append(matriz)
base_de_datos_javier = []
for i in range (62):
    path = os.path.join("Base de datos propia", "Javier", f"numero_{i}.png")
    matriz = conversor(path)
    base_de_datos_javier.append(matriz)
base_de_datos_felipe = []
for i in range (62):
    path = os.path.join("Base de datos propia", "Felipe", f"{i}.PNG")
    matriz = conversor(path)
    base_de_datos_felipe.append(matriz)
base_de_datos_antonia = []
for i in range (62):
    path = os.path.join("Base de datos propia", "Antonia", f"numero_{i}.jpg")
    matriz = conversor(path)
    base_de_datos_antonia.append(matriz)
base_de_datos_word = []
for i in range (62):
    path = os.path.join("Base de datos propia", "Word", f"numero_{i}.png")
    matriz = conversor(path)
    base_de_datos_word.append(matriz)
y_test_all = [i for i in range (62)]
for i in range (62):
    base_de_datos_ferra[i] = base_de_datos_ferra[i][0]
    base_de_datos_vicente[i] = base_de_datos_vicente[i][0]
    base_de_datos_javier[i] = base_de_datos_javier[i][0]
    base_de_datos_antonia[i] = base_de_datos_antonia[i][0]
    base_de_datos_felipe[i] = base_de_datos_felipe[i][0]
    base_de_datos_word[i] = base_de_datos_word[i][0]
