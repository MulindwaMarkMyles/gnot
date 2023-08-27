from django.shortcuts import render, get_object_or_404
from .models import Note


# Create your views here.
notes = Note.objects.all()


def app(request):
    return render(request, "index.html", {"notes": notes})


def addnotes(request):
    return render(request, "addnotes.html", {"notes": notes})


def viewnote(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, "viewnote.html", {"note": note})
