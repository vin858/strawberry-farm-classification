import cv2
import os
class divider:
   
    def __init__(self,img_path,save_dir):
        
        
        self.save_dir = save_dir
        self.img_path=img_path
        
    def divide(self,idx):
        save_dir =self.save_dir 
        img=cv2.imread(self.img_path,-1)
        self.idx=idx
        if len(img.shape)==2:
            chn=1
            hig,wid=img.shape
        else:    
            hig,wid,chn= img.shape
         
        #if img.shape[2]==4:
            #img=img[:,:,:3]
        
        for h in range(1,(int(hig/512)+1)):
             for w in range(1,(int(wid/512)+1)):
                  start_h=512*(h-1)
                  end_h=512*h
                  start_w=512*(w-1)
                  end_w=512*w
                  if chn==1:
                     image_i=img[start_h:end_h,start_w:end_w]
                    
                     cv2.imwrite(os.path.join(save_dir , 'rgb_elev_tile'+str(self.idx)+'.tif'),image_i)
                     self.idx=self.idx+1
                  else:
                     image_i=img[start_h:end_h,start_w:end_w,:]
                     
                     cv2.imwrite(os.path.join(save_dir , 'rgb_elev_tile'+str(self.idx)+'.tif'),image_i)
                     self.idx=self.idx+1
        #print(self.idx) 
        indx=self.idx
        return indx
