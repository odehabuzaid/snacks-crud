from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Snack(models.Model):
    title = models.CharField(max_length=256, help_text="Enter Snack Name")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    discription = models.TextField()
    
    def get_absolute_url(self):
        return reverse("snack_details", args=[str(self.id)])
