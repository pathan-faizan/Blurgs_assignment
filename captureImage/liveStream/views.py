

# Create your views here.
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip


from rest_framework.decorators import api_view
from rest_framework.response import Response

from apscheduler.schedulers.background import BackgroundScheduler
from . serializers import ImageSerializer
from . models import LiveImage



from . capture import videoCamera

def gen():
    # start(camera.camImage())
    while True:
        frame = videoCamera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

       
        
               
@gzip.gzip_page
@api_view(['GET'])
def image(request):
  
    try:
        return StreamingHttpResponse(gen(),content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        print("aborted")

@api_view(['GET'])
def getImage(request):
    images = LiveImage.objects.order_by('-id')[:10]
    serializer = ImageSerializer(images,many=True)
    return Response(serializer.data)       


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(videoCamera.camImage, 'interval', seconds=5,max_instances=3)
    scheduler.start()        
