from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View,ListView,
                                    TemplateView)
from . import models
from .models import ImageUpload
from imagecfr_app.forms import UploadImageForm

from imagecfr_app.mxnetdownload import predict
import json

# Create index view
def index_view(request):
    if request.method =='POST':
        #instantiate an uploadimageform object
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            #save form and reference as image_url
            image_url = form.save()
            #get the id of image_url and store within session
            request_id = image_url.id
            request.session['request_id'] = request_id
            #redirect
            return redirect('classify')
    else:
        form = UploadImageForm()
    return render(request,'imagecfr_app/index.html',{'form':form})



def display_data_view(request):
    #get the id from the last form uploaded by user
    request_id = request.session.get('request_id')
    #retrieve the instanse of uploadimage that pertains to request_id
    instance = get_object_or_404(ImageUpload,id=request_id)

    #get absolute path to instance
    print(instance.upload_pic.path)
    #run mxnet model on instance
    classifications = predict(instance.upload_pic.path)
    print(type(classifications))

    #get url
    url = instance.upload_pic.url
    #create context dictionary
    context = {'image_url': url,
                'image_name': instance.filename(),
                'classifications': classifications
                }
    #render view and create context dictionary
    return render(request,'imagecfr_app/classify.html',context)

def delete_pic(request):
    print('delete test test test')
    #get the id from the last form uploaded by user
    request_id = request.session.get('request_id')
    print('id:%d' % (request_id))
    #retrieve the instanse of uploadimage that pertains to request_id
    instance = get_object_or_404(ImageUpload,id=request_id)
    #delete instance and record
    instance.delete_ImageUpload()
    #delete session key
    return HttpResponse("deleted")
