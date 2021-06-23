from django.shortcuts import render, redirect
from .forms import Resume_info_forms
from django.views import View
from .models import Resume_info
from django.conf import settings
from django.http import response
from django.http.response import HttpResponse
import mimetypes
# Create your views here.


class Registration(View):
    def get(self, request):
        forms = Resume_info_forms
        objs = Resume_info.objects.order_by('-id')[:5]
        context = {
            'forms':forms,
            'data':objs
        }
        return render(request, 'registration.html', context)
    
    def post(self, request):
        forms = Resume_info_forms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
        return redirect('registration')

def resume_details(request, id):
    obj = Resume_info.objects.get(id=id)
    gender = ''
    if obj.gender =='o':
        gender="Others"
    elif obj.gender == 'm':
        gender = "Male"
    elif obj.gender == 'f':
        gender = "Female"
    context={
        'object':obj,
        'gender':gender
    }
    return render(request, 'details.html', context)



def download(request, id):
    obj = Resume_info.objects.get(id=id)
    f_name = str(obj.my_file)    
    file_path = settings.MEDIA_URL + f_name
    print(file_path, "PSTH")
    file_open = open(file_path, 'r')
    mime_type = mimetypes.guess_type(file_path)
    file_name = f_name[7:]
    response = HttpResponse(file_open, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response