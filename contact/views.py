from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render

from contact.models import Contact


# Create your views here.
class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'
    success_url = '/'
