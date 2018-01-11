from django.shortcuts import render
from .models import Note, Tag
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime 

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_notes=Note.objects.all().count()
    num_tags=Tag.objects.all().count()

    notes=Note.objects.all()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_notes':num_notes,'num_tags':num_tags, 'notes':notes},
    )

class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        
        notes=Note.objects.filter(owner=self.request.user).order_by('-date_created')
        context['notes'] = notes
        return context

class NotesByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Main page for user, no note open
    """
    model = Note
    template_name ='notes/note_list_user.html'
    #paginate_by = 10
    
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-date_created')


from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import UpdateNoteForm

@login_required
def update_or_delete_note(request, pk):
    """
    View function for note update
    """
    notes=Note.objects.filter(owner=request.user).order_by('-date_created')
    note=get_object_or_404(Note, pk = pk)    
    
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = UpdateNoteForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            if 'Save' in request.POST:
                note.title = form.cleaned_data['title']
                note.content = form.cleaned_data['content']
                note.save()
                return HttpResponseRedirect(request.path_info)

            elif 'Delete' in request.POST:    
                note.delete()
                return HttpResponseRedirect(reverse('my-notes'))
    else:
        form = UpdateNoteForm(initial={'title': note.title, 'content': note.content})     
    
    return render(request, 'notes/update_note.html', {'form': form, 'note':note, 'notes':notes})
    

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note
from django.contrib.auth.models import User

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'content', 'owner']
   
    def get_initials(self):
        return {
            'title':"enter title",
        }

    def form_valid(self, form):
        note = form.save(commit=False)
        note.owner = self.request.user
        note.date_created = datetime.date.today()
        note.save()
        return HttpResponseRedirect(reverse('my-notes'))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NoteCreate, self).get_context_data(**kwargs)
        
        notes=Note.objects.filter(owner=self.request.user).order_by('-date_created')
        context['notes'] = notes
        return context

