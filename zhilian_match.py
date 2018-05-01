import cv2

import numpy as np

import pytesseract

import os

# pic_no = '%d'%k + '.tif'
# spic_no ='ver.'+'normal'+'.exp'+'%d'%k + '.tif'

# print(pic_no)
# print(spic_no)

img = cv2.imread('b_00')



gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

print(type(gray_img))

# cv2.imshow('123',gray_img)


ref,grey_img = cv2.threshold(gray_img,15,255,cv2.THRESH_BINARY)

print(type(grey_img))

# grey_img = cv2.threshold(gray_img,20,255,cv2.THRESH_BINARY)


# cv2.waitKey(0)

# grey_img= cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,10)

upper_img = grey_img[0:85,0:280]

bottom_img = grey_img[85:130,0:280]

verify_img = grey_img[130:180,0:280]

segment_upper = list()

segment_bottom = list()

rearrange_upper = list()

rearrange_bottom = list()

rearrange_verify = list()

uplist = [11,18,15,9,2,10,5,3,4,13,20,16,12,14,7,1,6,8,17,19]

bottomlist = [16,7,18,15,3,11,10,14,4,8,5,12,20,13,19,2,1,17,9,6]

verilist = [16,7,18,15,3,11]

# tuple_bottom = ()


# for i in range(0,20):
#     tuple_bottom = tuple_bottom + tuple(rearrange_bottom[i])

for i in range(1,21):
    rearrange_upper.append(upper_img[0:85,14*uplist[i-1]-14:14*uplist[i-1]-1])
    rearrange_bottom.append(bottom_img[0:55,14*bottomlist[i-1]-14:14*bottomlist[i-1]-1])


for i in range(1,7):
    rearrange_verify.append(verify_img[0:50,14*verilist[i-1]-14:14*verilist[i-1]-1])

upper = np.column_stack((rearrange_upper[0],rearrange_upper[1],rearrange_upper[2],rearrange_upper[3],rearrange_upper[4],rearrange_upper[5],rearrange_upper[6],rearrange_upper[7],rearrange_upper[8],rearrange_upper[9],rearrange_upper[10],rearrange_upper[11],rearrange_upper[12],rearrange_upper[13],rearrange_upper[14],rearrange_upper[15],rearrange_upper[16],rearrange_upper[17],rearrange_upper[18],rearrange_upper[19],))
bottom = np.column_stack((rearrange_bottom[0],rearrange_bottom[1],rearrange_bottom[2],rearrange_bottom[3],rearrange_bottom[4],rearrange_bottom[5],rearrange_bottom[6],rearrange_bottom[7],rearrange_bottom[8],rearrange_bottom[9],rearrange_bottom[10],rearrange_bottom[11],rearrange_bottom[12],rearrange_bottom[13],rearrange_bottom[14],rearrange_bottom[15],rearrange_bottom[16],rearrange_bottom[17],rearrange_bottom[18],rearrange_bottom[19],))



# cv2.imshow('sd',grey_img)

# for i in range(1,21):
#     arrangeimg_upper = np.column_stack((arrangeimg_upper,segment_upper[i-1]))

veri = np.column_stack((rearrange_verify[0],rearrange_verify[1],rearrange_verify[2],rearrange_verify[3],rearrange_verify[4],rearrange_verify[5]))

rearrange_img = np.row_stack((upper,bottom))


# cv2.imshow('veri',veri)


# print(np.size(bottom,1))

# cv2.imshow('whole',rearrange_img)


# print(type(upper))

# cv2.waitKey(0)

# print(uplist[0])


# print(range(1,21))





# cv2.imwrite(spic_no,rearrange_img)

# adda = 'zhilian' + spic_no

# cmd = 'convert '+spic_no + ' -density 300 ' + adda

# print(cmd)

# os.system(cmd)

# print(vcode)

print(veri.shape)

First_char = veri[7:33,:]

Second_char = veri[:,:]

Third_char = verir[:,:]

Char_seq = ['First_char','Second_char','Third_char']


m = rearrange_img.shape(0)
n = rearrange_img.shape(1)

m0 = First_char.shape(0)
n0 = First_char.shape(1)

result = np.zeros([m-m0+1,n-n0+1])



