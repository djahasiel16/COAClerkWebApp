from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DocumentForm, FilterForm
from .models import Document


# Create your views here.
def index(request):
    docs = Document.objects.all().order_by('fund', 'doc_month')
    titles = [title[0] for title in DocumentForm.DOCUMENT_TITLE]
    funds = [fund[0] for fund in DocumentForm.FUND_CHOICES]
    offices = [office[0] for office in DocumentForm.OFFICE_CHOICES]

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('docsInventoryIndex')
        
    else:
        form = DocumentForm()

    return render(request, 'docsInventoryHandler/index.html', {'form': form, 'docs': docs, 'titles':titles, 'funds':funds, 'offices':offices})

def update_document(request, pk):
    doc = Document.objects.get(pk=pk)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            form.save()
            return redirect('docsInventoryIndex')
    else:
        form = DocumentForm(instance=doc)

    return render(request, 'docsInventoryHandler/forms/update_document.html', {'form':form, 'doc': doc})

def apply_filter(request):
    docs = Document.objects.all()
    titles = [title[0] for title in DocumentForm.DOCUMENT_TITLE]
    funds = [fund[0] for fund in DocumentForm.FUND_CHOICES]
    offices = [office[0] for office in DocumentForm.OFFICE_CHOICES]

    if request.method == 'POST':
        fund = request.POST['fund']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        title = request.POST['title']
        office = request.POST['office']

        filters = {'fund':fund, 'date_received__range':(startdate, enddate), 'title':title, 'office':office}

        if not startdate or not enddate:
            del filters['date_received__range']

        sanitized_filter = {k:v for k,v in filters.items() if v != ''}

        docs = Document.objects.filter(**sanitized_filter)

        try:
            titles.remove(title)
        except Exception as e:
            print(e)

        try:
            funds.remove(fund)
        except Exception as e:
            print(e)

        try:
            offices.remove(office)
        except Exception as e:
            print(e)
            print(office)

        print(sanitized_filter)
        return render(request, 'docsInventoryHandler/index.html', {'docs': docs,'filters':{'startdate':startdate, 'enddate':enddate, 'fund':fund, 'title':title, 'office':office}, 'titles':titles, 'funds':funds, 'offices':offices})
    else:
        form = DocumentForm()
        docs = Document.objects.all().order_by('fund', 'doc_month')
        return render(request, 'docsInventoryHandler/index.html', {'form': form, 'docs': docs, 'titles':titles, 'funds':funds, 'offices':offices})
