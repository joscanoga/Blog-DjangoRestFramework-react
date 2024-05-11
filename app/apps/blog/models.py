import uuid
from django.db import models
from django.utils import timezone

from apps.category.models import Category

# Create your models here.

def blog_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)

class Post(models.Model):
    """
    Modelo de los post del blog
    """
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        
    )
    blog_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField( unique=True)
    thumbnail = models.ImageField(upload_to=blog_directory_path)
    video = models.FileField(upload_to=blog_directory_path, blank=True, null=True)
    description = models.TextField()
    excerpt = models.TextField(max_length=100)
    
    #author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='draft')
    
    
    objects = models.Manager()#default manager
    postobjects = PostObjects()#custom manager
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title
    
    def get_video(self):
        if self.video:
            return self.video.url
        else:
            return ''
    
    def get_thumbnail(self):
        if self.thumbnail:  
            return self.thumbnail.url
        else:
            return ''
    