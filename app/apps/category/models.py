from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Modelo de las categorias de los post
    """
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,unique=True)
    thumbnail = models.ImageField(upload_to='media/categories/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return '/media/categories/default.png'
        
    