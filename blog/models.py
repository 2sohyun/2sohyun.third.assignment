from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)            # 타이틀
    pub_date = models.DateTimeField('date published')   # 날짜
    body = models.TextField()                           # 내용  
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name