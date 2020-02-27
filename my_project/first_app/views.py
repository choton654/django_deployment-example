from django.shortcuts import render
from django.http import HttpResponse
from . import models as md
from . import forms


# Create your views here.
def index(request):
   return render(request, 'first_app/index.html')


def about(request):
    web_page = md.AccessRecord.objects.order_by('date')
    my_dict = {'access_record': web_page}
    return render(request,"first_app/about.html",context=my_dict)

#def index1(request):
    #return HttpResponse('''<h1>Deep</h1> <a href="https://www.youtube.com"> Youtube</a>''')

def from_view(request):
    form = forms.FromName()
    my_form= {'myform':form}

    if request.method == "POST":
        form = forms.FromName(request.POST)

        if form.is_valid():
            print("validation successfull")
            print("NAME: "+form.cleaned_data["name"])
            print("EMAIL: "+form.cleaned_data["email"])
            print("TEXT: "+form.cleaned_data["text"])
            print("PASSWORD: "+form.cleaned_data["password"])

    return render(request,"first_app/form.html",{'myform':form})