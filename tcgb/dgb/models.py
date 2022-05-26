from django.db import models
class dgb(models.Model):
       tentrochoi = models.CharField(max_length=500)
       theloai = models.CharField(max_length=400)
       cachchoi = models.CharField(max_length=300)