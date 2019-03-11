from django.db import models

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post_uniqueCode = models.TextField()
    post_data = models.TextField()

    def __str__(self):
        return str(self.post_id) + "-" + str(self.post_date) + "_" + self.post_uniqueCode