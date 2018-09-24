from django.shortcuts import render, redirect
from notes.models import Note
from notes.forms import NoteForm
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='home:homepage')
def index(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {'notes': notes})

@login_required(login_url='home:homepage')
def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/detail.html', {'note': note})

@login_required(login_url='home:homepage')
def note_add(request):
    if request.user.is_authenticated:
        form = NoteForm()
        return render(request, 'notes/addnote.html', {'form': form})

@login_required(login_url='home:homepage')
def add_new_note(request):
    if request.method == 'POST':
        noteform = NoteForm(request.POST)
        if noteform.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            note = Note(user=request.user, title=title, description=description)
            note.save()
            return redirect('notes:index')



class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:index')
