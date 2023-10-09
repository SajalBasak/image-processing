import cv2

img = cv2.imread("apple2.jpg",0)
img2 = cv2.imread("orange2.jpg",0)

out_new=img.copy()

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

ab=1
b=0
print("a values")
for j in range(d,d+50):
    for i in range(img.shape[0]):
        c=ab*img.item(i,j)
        e=(1-ab)*img2.item(i,j)
        out_new.itemset((i,j),c+e)
        #print(ab)
    ab=ab-(1/50)

cv2.imshow("test check",out_new)

cv2.waitKey(0)

cv2.destroyAllWindows()