from django.shortcuts import render,redirect
from .models import ContactData

from django.shortcuts import render

from .forms import ContactForm

def temp_views(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')



def contect_view(request):
    if request.method == "POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():

            first_name = cform.cleaned_data.get('firstname')
            last_name = cform.cleaned_data.get('lastname')
            mobile = cform.cleaned_data.get('mobile')
            email = cform.cleaned_data.get('email')

            data = ContactData(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile=mobile,


            )
            data.save()
            cform = ContactForm()
            return render(request,'contact.html',{'cform': cform})
    else:
        cform = ContactForm()
        return render(request,'contact.html',{'cform': cform})






def galary_view(request):


    return render(request,'galary.html')
