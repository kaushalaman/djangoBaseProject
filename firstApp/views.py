from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import AccessRecord, WebPage, Topic
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_record': webpages_list}
    return render(request, 'firstApp/index.html', context=my_dict)
