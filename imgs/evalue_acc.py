from zhilian_ocr import zhilian_ocr

import cv2

for i in range(0,401):
    img_path = 'b_'+'%d'%i+'.png'

    img_veri_path = 's_'+'%d'%i+'.png'



    l = zhilian_ocr(img_path,img_veri_path)

    img = cv2.imread(img_path)

    l = l.astype(int)

    ll = cv2.line(img,(l[0,1],l[0,0]),(0,0),(0,0,255))

    cv2.line(img,(l[1,1],l[1,0]),(0,0),(0,255,0))

    cv2.line(img,(l[2,1],l[2,0]),(0,0),(255,0,0))

    save_name =  '%d'%i+'.png'
    cv2.imwrite(save_name,ll)