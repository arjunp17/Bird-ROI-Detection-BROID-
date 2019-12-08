import numpy as np
import cv2
import os

# bounding box txt file 1
b_b_test1 = np.loadtxt('../boundingbox_gt.txt',dtype='str')

# bounding box txt file 2
b_b_test2 = np.loadtxt('../boundingbox_pred.txt',dtype='str')

# image names
img_name_test1 = b_b_test1[:,0]
img_name_test2 = b_b_test2[:,0]

# x1_value and y1_value corresponds to top left corner of bounding box 1
x1_value_test1 = [int(i) for i in b_b_test1[:,1]]
y1_value_test1 = [int(i) for i in b_b_test1[:,2]]

# x1_value and y1_value corresponds to top left corner of bounding box 2
x1_value_test2 = [int(i) for i in b_b_test2[:,1]]
y1_value_test2 = [int(i) for i in b_b_test2[:,2]]

# width_value and height_value corresponds to width and height of bounding box 1
width_value_test1 = [int(i) for i in b_b_test1[:,3]]
height_value_test1 = [int(i) for i in b_b_test1[:,4]]

# width_value and height_value corresponds to width and height of bounding box 2
width_value_test2 = [int(i) for i in b_b_test2[:,3]]
height_value_test2 = [int(i) for i in b_b_test2[:,4]]

# x2_value and y2_value corresponds to bottom right corner of bounding box 1
x2_value_test1 = [x + y for x, y in zip(x1_value_test1, width_value_test1)]
y2_value_test1 = [x + y for x, y in zip(y1_value_test1, height_value_test1)]

# x2_value and y2_value corresponds to bottom right corner of bounding box 2
x2_value_test2 = [x + y for x, y in zip(x1_value_test2, width_value_test2)]
y2_value_test2 = [x + y for x, y in zip(y1_value_test2, height_value_test2)]

# path of imageset
path_test_image = '.../test' # path of original image
path_1 = '.../result' # path of predicted image

# array storing dice coefficients
dice_coefficient_for_all_images = []
img_name = []
# drawing bounding box and saving images
def draw_bounding_boxes_and_find_dice_coefficient(path_test,img_name1,img_name2,x1_test1,y1_test1,x2_test1,y2_test1,x1_test2,y1_test2,x2_test2,y2_test2,path_contest):
   for i in range(len(img_name1)):
      for j in range(len(img_name2)):
         if img_name1[i] == img_name2[j] and x1_test2[j] > 0.0 and y1_test2[j] > 0.0:
           print 'match found: continue process ..'
           img = cv2.imread(os.path.join(path_test,img_name1[i]), 1)
           cv2.rectangle(img, (x1_test1[i],y1_test1[i]), (x2_test1[i],y2_test1[i]), (255,0,0), 5)
           cv2.rectangle(img, (x1_test2[j],y1_test2[j]), (x2_test2[j],y2_test2[j]), (0,255,0), 5)
           b_b_1_area = (x2_test1[i]-x1_test1[i])*(y2_test1[i]-y1_test1[i])
           b_b_2_area = (x2_test2[j]-x1_test2[j])*(y2_test2[j]-y1_test2[j])
           if(min(x2_test1[i],x2_test2[j]) < max(x1_test1[i],x1_test2[j]) or min(y2_test1[i],y2_test2[j]) < max(y1_test1[i],y1_test2[j])):
              intersect_area = 0
           else:
              intersect_area = (min(x2_test1[i],x2_test2[j]) - max(x1_test1[i],x1_test2[j]))*(min(y2_test1[i],y2_test2[j]) - max(y1_test1[i],y1_test2[j]))
              cv2.rectangle(img, (max(x1_test1[i],x1_test2[j]),max(y1_test1[i],y1_test2[j])), (min(x2_test1[i],x2_test2[j]),min(y2_test1[i],y2_test2[j])), (0,0,255), 5) 
           dice_coef = 2*np.divide(intersect_area,np.add(b_b_1_area,b_b_2_area),dtype=float)
           dice_coefficient_for_all_images.append(dice_coef)
           img_name.append(img_name1[i])
           cv2.imwrite(os.path.join(path_contest,img_name1[i]),img)
            



            
draw_bounding_boxes_and_find_dice_coefficient(path_test_image,img_name_test1,img_name_test2,x1_value_test1,y1_value_test1,x2_value_test1,y2_value_test1,x1_value_test2,y1_value_test2,x2_value_test2,y2_value_test2,path_1)


print 'max dice_coef value is', max(dice_coefficient_for_all_images)
print 'min dice_coef value is', min(dice_coefficient_for_all_images)

dice_coefficient_for_all_images = np.array(dice_coefficient_for_all_images)
print 'index of max dice_coef value', dice_coefficient_for_all_images.argmax()
print 'index of min dice_coef value', dice_coefficient_for_all_images.argmin()
print 'mean_dice_coef is', np.mean(dice_coefficient_for_all_images)
print 'sum_dice_coef is', np.sum(dice_coefficient_for_all_images)
print 'standard_deviation_dice_coef is', np.std(dice_coefficient_for_all_images)

np.savetxt('dice_coef.txt',dice_coefficient_for_all_images,fmt='%s')
np.save('dice_coef', dice_coefficient_for_all_images)

np.argwhere( dice_coefficient_for_all_images==0)
dice_coefficient_for_all_images_asc = sorted(dice_coefficient_for_all_images)

