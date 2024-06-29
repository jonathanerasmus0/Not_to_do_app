from django.db import models
from django.contrib.auth.models import User

class NotTODO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    context = models.CharField(max_length=100)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    repeat_interval = models.CharField(max_length=10, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], null=True, blank=True)
    shared_with = models.ManyToManyField(User, related_name='shared_nottodos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Comment(models.Model):
    nottodo = models.ForeignKey(NotTODO, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
