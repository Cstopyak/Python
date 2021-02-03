from django.db import models
import re

class UserManager(models.Manager):
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        userswithSameusername = User.objects.filter(username = postData['username'])
        

        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 2:
            errors["namereq"] = "name is Required"

        if len(postData['username']) == 0:
            errors["userreq"] = "Username is Required"

        
        elif len(userswithSameusername)>0:
            errors ['usernametaken'] = "Try another username."

        if len(postData['pass']) == 0:
            errors["passreq"] = "Password is Required"
        
        elif len(postData['pass']) < 8:
            errors["passreq"] = "8 characters required for password"

        if postData['pass'] != postData['confpass']:
            errors["confpassmatch"] = "Password must match"

        
        
        return errors

class itemManager(models.Manager):
    def createItemVal(self, postData):
        errors = {}
        if len(postData['item/product']) == 0:
            errors["itemreq"] = "Please put in an item you want."
            
        return errors


    def loginValidation(self, postData):
        errors = {}

        userswithSameusername = User.objects.filter(username = postData['username'])
        if len(userswithSameusername) == 0:
            errors ['usernamenotregistered'] = "Please register your User Name"
        else:
            print(userswithSameusername[0].password)
        if userswithSameusername[0].password != postData['pass']:
            errors['incorrectpassword'] = "Incorrect Password. Please put correct password in."

        return errors



class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    

class item(models.Model):
    item_name = models.CharField(max_length=255)
    created_item = models.ForeignKey(User, related_name = 'user_created', on_delete = models.CASCADE)
    wishlisted = models.ManyToManyField(User, related_name = 'users_favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = itemManager()
    
