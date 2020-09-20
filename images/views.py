from django.shortcuts import render
import os
from django.http import HttpResponse, Http404

# Create your views here.


def index(request):
    flPath = os.listdir('catImages')
    return render(request, 'images/index.html', {'path': flPath})



def downloadImage(request, path):

    imagePath = 'catImages/'

    file_path = os.path.join(imagePath, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404