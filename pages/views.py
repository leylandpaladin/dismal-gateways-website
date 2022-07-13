from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Feedback
from .forms import FeedbackForm
def homepage_view(request,*args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args,**kwargs):

    form = FeedbackForm()
    if request.method == "POST":

        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Feedback.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
            'form':form
            }
    return render(request,'contact.html', context)


def about_view(request, *args, **kwargs):
    my_context = {
            "text": "This is about us",
            "smth_else": 'else',
            "test_list": ('monkey', 'apple', 'boobs', 22, 'gowno')
            }
    return render(request, 'about.html', my_context)


def products_view(request, *args, **kwargs):
    return render(request, 'products.html', {})
