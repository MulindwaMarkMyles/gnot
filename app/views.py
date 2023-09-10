from django.shortcuts import render, get_object_or_404, redirect
from .models import Note


# Create your views here.
notes = Note.objects.all()


def app(request):
    return render(request, "index.html", {"notes": notes})


def addnotes(request):
    if request.method == "POST":
        note_title = request.POST["note_title"]
        the_note = request.POST["the_note"]
        if the_note:
            theNote = Note(title=note_title, content=the_note)
            theNote.save()
            return redirect("home_page")
        else:
            return render(request, "addnotes.html")
    else:
        return render(request, "addnotes.html")


def viewnote(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, "viewnote.html", {"note": note})
