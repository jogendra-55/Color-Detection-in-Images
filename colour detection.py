# Importing required libraries and attributes.
from tkinter.font import names
import cv2 
import pandas as pd
 
# Reading Image
img=cv2.imread('pic1..jpg') 
img=cv2.resize(img,(600,400)) 

clicked=False   
r=g=b=x_pos=y_pos=0

# Labelling and reading Dataset 
index=["color","color_name","hex","R","G","B"]
df=pd.read_csv('colors.csv',names=index,header=None)


def print_color_name(R,G,B):
    minm=10000
    for i in range(len(df)):
        c=abs(R-int(df.loc[i,"R"])) + abs(G-int(df.loc[i,"G"])) + abs(B-int(df.loc[i,"B"]))
        if c<=minm:
            minm=c
            cname=df.loc[i,"color_name"]
    return cname

def event_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', event_function)

while True:
    cv2.imshow("Image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (525, 65), (b, g, r), -1)
        text = print_color_name(r, g, b) + ' (' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_4)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_8)
        clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()



