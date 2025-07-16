from django.db import models
from django.contrib.auth.models import User

class DevTool(models.Model):
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name


class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='idea_thumbnails/')
    content = models.TextField()
    interest = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name='ideas')

    def __str__(self):
        return self.title


class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'idea')  # 한 유저가 한 아이디어에 한 번만 찜 가능

    def __str__(self):
        return f"{self.user.username} - {self.idea.title}"
