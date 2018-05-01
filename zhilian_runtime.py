import cv2

import numpy as np

import pytesseract


def zhilian_ocr(img_path,veri_img_path):



    img = cv2.imread(img_path)

    veri_img = cv2.imread(veri_img_path)

    grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    grey_veri_img = cv2.cvtColor(veri_img,cv2.COLOR_RGB2GRAY)

    # ref,binary_img = cv2.threshold(grey_img,15,255,cv2.THRESH_BINARY)
    binary_veri_img = grey_veri_img

    binary_img = grey_img
    # ref,binary_veri_img =cv2.threshold(grey_veri_img,15,255,cv2.THRESH_BINARY)


    first_char = binary_veri_img[6:33,11:34]


    second_char = binary_veri_img[6:33,34:55]

    third_char = binary_veri_img[6:33,54:77]

    char_seq = (first_char,second_char,third_char)

    location = np.zeros([3,2])


    # cv2.imshow('1',second_char)
    for no in range(0,3):

        m = binary_img.shape[0]
        n = binary_img.shape[1]

        m0 = char_seq[no].shape[0]
        n0 = char_seq[no].shape[1]

        result = np.zeros([m-m0+1,n-n0+1])


        vec_sub = char_seq[no].reshape(m0*n0,order='F')

        vec_sub.shape = (vec_sub.shape[0],1)
        norm_sub = np.linalg.norm(vec_sub)


        for i in range(0,m-m0+1):
            print i
            for j in range(0,n-n0+1):
                subMatr = binary_img[i:(i+m0),j:(j+n0)]

                # print(subMatr.shape[1])
                # cv2.imshow('1',subMatr)
                # cv2.waitKey(0)
                vec = subMatr.reshape((subMatr.shape[0])*(subMatr.shape[1]),order = 'F')
                # vect = np.zeros([(subMatr.shape[0])*(subMatr.shape[1])])
                vec = np.array(vec)
                vec.shape = (vec.shape[0],1)
                vect = vec.T
                # sum_ = 0
                # print type(vect[0,0])
                # print vec_sub[0,0]
                # for l in range(0,vec.shape[0]):
                # print (np.dot(vect[0,0],vec_sub[0,0]))
                    # sum_ = sum_ + vect[0,l]*vec_sub[l,0]
                # for k in range(0,(subMatr.shape[0])*(subMatr.shape[1])):
                #     vect[k,0] = vec[0,k]
                vect = vect.astype(float)
                vec_sub = vec_sub.astype(float)
                result[i,j] = np.dot(vect,vec_sub)/(np.linalg.norm(vec)*norm_sub+np.spacing(1))
                # print np.multiply(vect,vec_sub)
                # print np.asmatrix(vect)*np.asmatrix(vec_sub)
                # print sum_
                # print vec_sub

                # print np.linalg.norm(vec)
            # [x,y]= np.where(np.max(result))
        x,y = np.where(result==np.max(result))

        print result
        res = grey_img[x[0]:x[0]+m0,y[0]:y[0]+n0]
        location[no,0] = x[0]+m0/2
        location[no,1] = y[0]+m0/2

