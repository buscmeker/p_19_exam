from django.shortcuts import render

from apps.models import Contact


# Create your views here.
def index_1(request):
    Contacts = Contact.objects.all()
    context = {
        'Contacts': Contacts
    }
    return render(request, 'apps/index.html', context)