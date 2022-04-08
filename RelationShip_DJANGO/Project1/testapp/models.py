from django.db import models

# Create your models here.

<<<<<<< HEAD
class Category(models.Model):
    cat_name = models.CharField(max_length=32)

    def __str__(self):
        return self.cat_name


class Author(models.Model):
    auth_name = models.CharField(max_length=32)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.auth_name

class Book(models.Model):
    book_name = models.CharField(max_length=32)
    book_description = models.CharField(max_length=30,null=True,blank=True)
    auth = models.ManyToManyField(Author,related_name='all_authors',blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.book_name

    def authors(self):
        return ','.join([str(a) for a in self.auth.all()])




=======
class Book(models.Model):

    book_name = models.CharField(max_length=32)
    book_description = models.CharField(max_length=30)


class Author(models.Model):

    auth_name = models.CharField(max_length=32)
    email = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)


class Category(models.Model):

>>>>>>> 3c8c858274347881ab6e0e59087e4fea704ae490





