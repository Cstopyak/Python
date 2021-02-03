from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<User Object: {self.first_name} ({self.id})"

class Item(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    favoritors = models.ManyToManyField(User, related_name = "items_favorited")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<Item Object: {self.name} ({self.id})"


# <Item: Item object (1)>