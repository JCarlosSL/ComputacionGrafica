from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('succes')
        else:
            form=DocumentForm()
        return render(request, 'pointOperator/index.html',{'form':form})

def success(request):
    return HttpResponse('successfully uploaded')
