from Divider_idx import divider
import cv2
import os
img_path='E:/ai project/mahabaleshwar/output13.tif'

save_dir='E:/ai project/mahabaleshwar/clip13'
idx=1
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

print(img_path)
test_imgs= divider(img_path, save_dir)
indx=test_imgs.divide(idx)
idx=indx