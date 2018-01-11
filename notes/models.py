from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    """
    Model representing a note tag.
    """
    name = models.CharField(max_length=200, help_text="Enter a tag name:")
    
    def __str__(self):
        """
        String for representing the Model object 
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Note(models.Model):
    """
    Model representing a note.
    """
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    content = models.TextField(help_text="Enter text here")
    tag = models.ManyToManyField(Tag, help_text="Select a tag for this note")
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular note instance.
        """
        return reverse('note-detail', args=[str(self.id)])


