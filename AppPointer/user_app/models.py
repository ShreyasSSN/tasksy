from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    app_name = models.CharField(max_length=100)
    screenshot = models.ImageField()
    points = models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.screenshot.delete(save=False)  # Delete the file
        super().delete(*args, **kwargs)