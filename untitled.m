clear
clc
Rearrangement_img = imread('b_6.png');

Rearrangement_img = rgb2gray(Rearrangement_img);

Rearrangement_verify = imread('s_6.png')

Rearrangement_verify = rgb2gray(Rearrangement_verify)

First_char = Rearrangement_verify(7:33,12:34);

Second_char = Rearrangement_verify(7:33,34:55);

Third_char = Rearrangement_verify(7:33,55:77);

Char_seq = {First_char,Second_char,Third_char};


for k = 1:3
    

reource_p=Rearrangement_img;
reource_p_sub=Char_seq{k};  
[m,n]=size(reource_p);  
[m0,n0]=size(reource_p_sub);  
result=zeros(m-m0+1,n-n0+1);  
vec_sub = double( reource_p_sub(:) );  
norm_sub = norm( vec_sub );  
for i=1:m-m0+1  
    for j=1:n-n0+1  
        subMatr=reource_p(i:i+m0-1,j:j+n0-1);  
        vec=double( subMatr(:) );  
        result(i,j)=vec'*vec_sub / (norm(vec)*norm_sub+eps);  
    end  
end  
%找到最大相关位置  
[iMaxPos,jMaxPos]=find( result==max( result(:)));  
figure,  
subplot(121);imshow(reource_p_sub),title('匹配模板子图像');  
subplot(122); 
imshow(reource_p);  
title('标记出匹配区域的原图'),  
hold on  
plot(jMaxPos,iMaxPos,'*');%绘制最大相关点  
 %用矩形框标记出匹配区域  
plot([jMaxPos,jMaxPos+n0-1],[iMaxPos,iMaxPos]);  
plot([jMaxPos+n0-1,jMaxPos+n0-1],[iMaxPos,iMaxPos+m0-1]);  
plot([jMaxPos,jMaxPos+n0-1],[iMaxPos+m0-1,iMaxPos+m0-1]);  
plot([jMaxPos,jMaxPos],[iMaxPos,iMaxPos+m0-1]);  

end
