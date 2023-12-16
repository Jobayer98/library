from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    
    context = {
        'num_books':num_books,
        'num_instance': num_instance,
    }
    
    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    
    
class BookDetail(DetailView):
    model = Book
    