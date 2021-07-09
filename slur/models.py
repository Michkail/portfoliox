from django.db import models

# Create your models here.
class BackStellar(models.Model):
    nich = models.CharField(max_length=40, blank=None)
    kelempiau = models.CharField(max_length=75, blank=True)
    khinzir = models.CharField(max_length=150, blank=True)
    wacktu = models.DateTimeField(auto_now_add=True)
    pitjture = models.ImageField(upload_to="bglur")

    def __str__(self):
       return "{}. {}".format(self.id, self.nich)
# self.id untuk menampilkan data menurut id database
