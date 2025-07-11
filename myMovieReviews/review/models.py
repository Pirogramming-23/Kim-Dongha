from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Post(models.Model):
    GENRE_CHOICES = [
        ('action', '액션'),
        ('comedy', '코미디'),
        ('drama', '드라마'),
        ('horror', '호러'),
        ('romance', '로맨스'),
        ('sci-fi', 'SF'),
        ('thriller', '스릴러'),
        ('ani', '애니메이션')
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    year = models.IntegerField(
        default = 2024
    )
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    gamdok = models.CharField(max_length=50)
    juyeon = models.CharField(max_length=200)
    runningtime = models.IntegerField(
        default = 120
    )
    score = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    text = models.TextField()
    text_content = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title