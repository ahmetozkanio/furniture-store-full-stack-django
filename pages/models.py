from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.

class About(models.Model):
    description = RichTextField()
  
class Fair(models.Model):
    name =  models.CharField(max_length = 256, null = True,)
    description = RichTextField(blank =True, null = True)
    image = models.ImageField(upload_to ='fairs/image/%Y/%m/%d/',null = True)
    date = models.DateField(null = True)
    slug = models.SlugField(blank =True,null = True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class FairImage(models.Model):
    fair = models.ForeignKey(Fair, related_name='fair_image', on_delete= models.CASCADE)
    image = models.ImageField(upload_to ='fair/images/%Y/%m/%d/',null=True,blank= True)
    def __str__(self):
        return self.fair.name