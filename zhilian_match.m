clear;close all
clc
Original_img = imread('16.jpg');
Original_gray = rgb2gray(Original_img);
Original_gray = im2bw(Original_gray,0.05);
Upper_img = Original_gray(1:85,:);
Bottom_img = Original_gray(86:170,:);
Segment_upper = {};
Segment_bottom = {};
Rearrangement_upper = [];
Rearrangement_bottom = [];
Rearrangement_verify = [];
Rearrangement_img = [];

%%
for i = 1:20
    Segment_upper{i} = Upper_img(:,14*i-13:14*i);
    Segment_bottom{i} = Bottom_img(:,14*i-13:14*i);
end

Rearrangement_upper=[Segment_upper{11},Segment_upper{18},Segment_upper{15},Segment_upper{9},Segment_upper{2},Segment_upper{10},Segment_upper{5},Segment_upper{3},Segment_upper{4},Segment_upper{13},Segment_upper{20},Segment_upper{16},Segment_upper{12},Segment_upper{14},Segment_upper{7},Segment_upper{1},Segment_upper{6},Segment_upper{8},Segment_upper{17},Segment_upper{19}];

Rearrangement_bottom=[Segment_bottom{16},Segment_bottom{7},Segment_bottom{18},Segment_bottom{15},Segment_bottom{3},Segment_bottom{11},Segment_bottom{10},Segment_bottom{14},Segment_bottom{4},Segment_bottom{8},Segment_bottom{5},Segment_bottom{12},Segment_bottom{20},Segment_bottom{13},Segment_bottom{19},Segment_bottom{2},Segment_bottom{1},Segment_bottom{17},Segment_bottom{9},Segment_bottom{6}];

Rearrangement_img = [Rearrangement_upper;Rearrangement_bottom];

Rearrangement_img = Rearrangement_img(1:130,:);

Rearrangement_verify={16},Segment_bottom{7},Segment_bottom{18},Segment_bottom{15},Segment_bottom{3},Segment_bottom{11}];
%%
% imshow(Rearrangement_upper)
% figure
% imshow(Rearrangement_bottom)
% figure
% imshow(Rearrangement_img)
% figure
%%

Rearrangement_verify = Rearrangement_verify(54:78,11:75);

First_char = Rearrangement_verify(:,1:23);

Second_char = Rearrangement_verify(:,23:44);

Third_char = Rearrangement_verify(:,44:65);

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
