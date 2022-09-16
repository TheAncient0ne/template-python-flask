import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# def edicão_placa(img2):
#     img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#     imgcorte_alt_alt = int(img.shape[0] * 0.33)
#     imgcorte_alt_baix = int(img.shape[0] * 0.87)
#     imgcorte_lad_dir = int(img.shape[1] * 0.07)
#     imgcorte_lad_esq = int(img.shape[1] * 0.97)
#     recorte = img[imgcorte_alt_alt:imgcorte_alt_baix, imgcorte_lad_dir:imgcorte_lad_esq]
#     cv2.imshow("recorte", recorte)
#     suave = cv2.GaussianBlur(recorte, (3, 3), 10)
#     T = mahotas.thresholding.otsu(suave)
#     temp = recorte.copy()
#     temp[temp > T] = 255
#     temp[temp < 255] = 0
#     temp = cv2.bitwise_not(temp)
#     blur_mediana = cv2.medianBlur(temp, 13)
#     blur = cv2.blur(blur_mediana, (9, 21))
#     cv2.imwrite("Placa filtrada.jpg", blur)
#     return blur
