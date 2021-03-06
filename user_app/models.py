from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email']='Please provide a valid email address'

        if len(post_data['first_name'])<2:
            errors['first_name']='First name should be at least 2 characters'
        if len(post_data['first_name'])>50:
            errors['first_name']='First name should be less than 50 characters'

        if len(post_data['last_name'])<2:
            errors['last_name']='Last name should be at least 2 characters'
        if len(post_data['last_name'])>50:
            errors['last_name']='Last name should be less than 50 characters'
        
        try: 
            User.objects.get(email=post_data['email'])
            errors ['email']="Email address already in use"
        except:
            pass
        
        if len(post_data['password'])<3:
            errors['password']='Password should be at least 3 characters'
        if post_data['password'] != post_data ['confirm_password']:
            errors['confirm_password']='Passwords do not match'
        if len(post_data['description'])>50:
            errors['description']='Description must be less than 50 characters'
        return errors

    def info_validator(self, post_data, user):
        errors={}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email']='Please provide a valid email address'

        if len(post_data['first_name'])<2:
            errors['first_name']='First name should be at least 2 characters'
        if len(post_data['first_name'])>50:
            errors['first_name']='First name should be less than 50 characters'

        if len(post_data['last_name'])<2:
            errors['last_name']='Last name should be at least 2 characters'
        if len(post_data['last_name'])>50:
            errors['last_name']='Last name should be less than 50 characters'
        
        if  user.email != post_data['email'] and User.objects.get(email = post_data['email']):
            errors ['email']="Email address already in use"

        return errors

    def description_validator(self, post_data):
        errors={}
        if len(post_data['description'])>50:
            errors['description']='Description must be less than 50 characters'
        return errors


    def password_validator(self, post_data):
        errors={}
        if len(post_data['password'])<3:
            errors['password']='Password should be at least 3 characters'
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password']='Passwords do not match'
        return errors

class CommentManager(models.Manager):
    def commentValidator(self, post_data):
        errors = {}
        if len(post_data['comment'])<2:
            errors['comment'] = 'Comment must be at least 2 characters long.'
        return errors

class MessageManager(models.Manager):
    def messageValidator(self, post_data):
        errors={}
        if len(post_data['message'])<2:
            errors['message'] = 'Message must be at least 2 characters long'
        return errors



class User(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    description = models.TextField()
    admin=models.BooleanField()
    email=models.CharField(max_length=254)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Message(models.Model):
    message=models.TextField()
    user_page=models.ForeignKey(User, related_name='page', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=MessageManager()

class Comment(models.Model):
    comment=models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message=models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

