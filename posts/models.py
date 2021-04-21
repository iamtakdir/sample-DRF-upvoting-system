
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField()
    poster = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

class Vote (models.Model):
    voter = models.ForeignKey(User,on_delete=CASCADE)
    post = models.ForeignKey(Post,on_delete=CASCADE)

    def __str__(self):
        return str(self.voter)