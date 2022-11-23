import cv2
from django.views.decorators import gzip
from datetime import datetime
import os
from .serializers import ImageSerializer


class SingleTon(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            orig = super(SingleTon,cls)
            cls._instance = orig.__new__(cls,*args,**kw)
            
            return cls._instance
        

class VideoCamera(SingleTon):

    
    video = cv2.VideoCapture(0)
    res,image = None,None
        
    def __del__(self):
        self.video.release()

    def get_frame(self):
        self.res,self.image = self.video.read()
        ret,jpeg = cv2.imencode('.jpg',self.image)
        return jpeg.tobytes()

    

    def camImage(self):
        
        if self.res!=None:
            now = datetime.now()
            timestamp = str(now.timestamp())

            cv2.imwrite(os.path.join(os.getcwd()+'/static','image_'+timestamp+'.png'), self.image)
            serializer = ImageSerializer(data={'image':'static/image_'+timestamp+'.png'})
            if serializer.is_valid():
               serializer.save()
            print("image captured") 


videoCamera = VideoCamera()