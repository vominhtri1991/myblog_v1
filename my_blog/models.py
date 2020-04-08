from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

Blog_Type=(('L','Linux-Unix'),('V','VMWare'),('W','Window'),('P','Python'),('S','Scripting'),('O','Others'))
class Blog(models.Model):
	title=models.CharField(max_length=120)
	description=models.CharField(max_length=120)
	date=models.DateField()
	content=models.TextField()
	new_content=RichTextUploadingField()
	type_blog=models.CharField(max_length=29,choices=Blog_Type,default='L')
	def __str__(self):
		return "Blog "+str(self.id)+": "+self.title


# Create your models here.
