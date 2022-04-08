from django import forms
from .models import Book, Author, Category
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'book_name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Agnipankh',
                }
            ),
            'model_name': forms.PasswordInput(),

        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'