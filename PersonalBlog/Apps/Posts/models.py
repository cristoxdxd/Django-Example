from django.db import models
from datetime import date


# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, default='No Title')
    description = models.TextField(max_length=5000, default='Description not available')
    date = models.DateField("Date", default=date.today)


    def get_all_posts(self):
        return list(Posts.objects.all())


    def make_post(self, newtitle, newdescription):
        Posts.objects.create(title=newtitle, description=newdescription)
