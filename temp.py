# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:52:28 2020

@author: NLP Lab
"""

import numpy as np
import cv2
import math


img = cv2.imread("apple2.jpg",0)
img2 = cv2.imread("orange2.jpg",0)

out_neg= img.copy()

out_log= img.copy()


out_pl= img.copy()

out_new=img.copy()

out_new2=img2.copy()


cv2.imshow("input image",img)
cv2.imshow("orange",img2)

print(img.max())
print(img.min())
print(img.shape)

#help(math.log)

print(img.shape[1])
d=(img.shape[1])/2
print(d)
d=d-25
d=(int)(d)
print(d)
print(img.shape[0])

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if j<d:
            continue
        elif j>=d+50:
            a=img2.item(i,j)
            out_new.itemset((i,j),a)
        #out_neg.itemset((i,j),255-a)
        
        #out_log.itemset((i,j),32*math.log(a+1,2))
        
        #out_pl.itemset((i,j),(255/math.pow(255,4))*math.pow(a,4))

#cv2.imshow("negative image",out_neg)

#cv2.imshow("log image",out_log)

#cv2.imshow("power law image",out_pl)

ab=1
b=0
print("a values")
for j in range(d,d+50):
    for i in range(img.shape[0]):
        c=ab*img.item(i,j)
        d=(1-ab)*img2.item(i,j)
        out_new.itemset((i,j),c+d)
        #print(ab)
    ab=ab-(1/50)

cv2.imshow("test check",out_new)

cv2.waitKey(0)

cv2.destroyAllWindows()