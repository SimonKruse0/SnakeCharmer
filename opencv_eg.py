import cv2
img = cv2.imread("EZ_16-10-21_Stige_9391_small.jpg", cv2.IMREAD_COLOR)

#cv2.imshow("Eivind", img)
#cv2.waitKey()

img[100, 100] = [0, 0, 0]

cv2.imwrite("output.jpg", img)

