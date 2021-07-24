from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
	judul = models.CharField(max_length = 255)
	isi = RichTextField(blank = True, null = True)
	# isi = models.CharField(max_length = 1000)
	tanggal = models.DateField(auto_now_add = True)