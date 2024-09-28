from django.db import models

# Create your models here.
#django provides built in user registration
class Post(models.Model):
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name = 'posts')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='', blank=True)
    body = models.TextField(default='', blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name = 'comments')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default='', blank=False)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created']

class Category(models.Model):
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name = 'categories')
    name = models.CharField(max_length=100, blank=False, default='')
    posts = models.ManyToManyField('Post', related_name='categories')
        


