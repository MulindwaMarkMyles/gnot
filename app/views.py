from django.shortcuts import render
from .models import Note


# Create your views here.
def app(request):
    notes = Note.objects.all()
    return render(request, "index.html", {"notes": notes})

def addnotes(request):
    return render(request, "addnotes.html")