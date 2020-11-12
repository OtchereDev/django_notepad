from django.shortcuts import render,get_object_or_404,redirect
from .models import Note
from .forms import NoteForm



def note_list_view(request):
    notes= Note.objects.filter(finished=False)
    finshed=Note.objects.filter(finished=True)
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={
        'notes':notes,
        'finish_items':finshed,
        'form':form,
    }
    return render(request, 'note_list.html',context)

def finish_item(request,pk):
    note=get_object_or_404(Note,id=pk)
    note.finished=True
    note.save()
    return redirect('/')

def recover_item(request,pk):
    note=get_object_or_404(Note,id=pk)
    note.finished=False
    note.save()
    return redirect('/')

def delete_item(request,pk):
    note=get_object_or_404(Note,id=pk)
    note.delete()
    return redirect('/')