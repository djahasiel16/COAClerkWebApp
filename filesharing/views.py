from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MultiDocumentForm
from .models import MultiDocument

# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = MultiDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = MultiDocumentForm()

    files = MultiDocument.objects.all()

    return render(request, "filesharing/upload.html", {'form':form, 'files':files})

def success(request):
    return render(request, 'filesharing/success.html')

