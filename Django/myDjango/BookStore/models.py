from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    STREAM_TYPE = [
        ('SD', 'Software Development'),
        ('DS', 'Data Science'),
        ('CS', 'Cyber Security'),
    ]
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    stream = models.TextField(max_length=3, choices=STREAM_TYPE)
    details = models.TextField(max_length=100)
    image = models.ImageField(default='', upload_to='images/')

    def __str__(self):
        return self.name
    
# one to many relationship
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    review = models.TextField(max_length=100)
    date_time = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.review[:50] + '...' if len(self.review) > 50 else self.review
    
# many to many relationship
class BookStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='bookStores')
    
    def __str__(self):
        return self.name
    
# one to one relationship
class BookAuthor(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_author')
    bio = models.TextField(max_length=500)
    
    def __str__(self):
        return self.book.name