from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)
def LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/templates/relationship_app/register.html'
    success_url = reverse_lazy('login')

    
