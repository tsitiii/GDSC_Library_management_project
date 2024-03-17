from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    book_file=models.FileField(upload_to='books_pdfs', default= "")
    book_cover=models.ImageField(upload_to='library_manage/books_image', default = "")
    ratings=models.DecimalField(max_digits=3, decimal_places=1, default = 2)
    status_choices = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='available')
     

    def calculate_average_rating(self):
    
        # Calculate the average rating based on related reviews
        reviews = self.review_set.all()
        if reviews:
            total_ratings = sum(review.rating for review in reviews)
            average_rating = total_ratings / len(reviews)
            self.ratings = average_rating
        else:
            self.ratings = None
        self.save()


    def __str__(self):
        return self.title 
