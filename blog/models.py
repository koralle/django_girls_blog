from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Post(models.Model):
  # 記事作成者
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  # 記事タイトル
  title = models.CharField(max_length=200)
  # 記事本文
  text = models.TextField()
  # 記事作成日
  created_date = models.DateTimeField(default = timezone.now)
  # 記事投稿日
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title