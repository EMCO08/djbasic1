from django.db import models

# Create your models here.
class Not(models.Model):
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.icerik[:50]
