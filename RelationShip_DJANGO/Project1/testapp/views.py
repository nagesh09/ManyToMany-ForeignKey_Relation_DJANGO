from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def homeView(request):
    template_name = 'base.html'
    context ={}
    return render(request,template_name,context)

def addBooksView(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'testapp/addbooks.html'
    context = {'form':form}
    return render(request,template_name,context)

def showBooksView(request):
    template_name = 'testApp/showallbooks.html'
    books = Book.objects.all()
    print(books) # Return Query set of books
    for book in books: # Get single book from queryset
        print(book.cat) # print single book category (which if foreign key relationship), we access directly with book obj.field_name
        for auth in book.auth.all(): # to access auth(ManyToMany) from book itrate book obj with (obj.manytomany_field_in_bokk_table.all())
            print(book)
            print(auth) # we get all authors for that particular book
    context = {'books':books}
    return render(request,template_name,context)



def updateBookView(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form. is_valid():
            form.save()
            return redirect('show')
    template_name = 'testApp/addbooks.html'
    context = {'form': form}
    return render(request, template_name, context)

