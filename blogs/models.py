from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class BlogCategory(models.Model):
    category= models.CharField(max_length=20 , null=True)
    slug = models.SlugField(max_length=20, unique=True ,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse ('blogs_by_category', args=[self.slug])   

    def __str__(self):
        return self.category

    # def get_count(self):
    #     return Blog.objects.filter(category=self).count()

    class Meta:
        verbose_name_plural = "Blog Categoires"
        verbose_name = "Blog Categoires" # 1 space


class Blog(models.Model):
    status_list = [
        ('Draft','Draft'),
        ('Published','Published'),
        ('Closed','Closed')

    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,null=True)
    author = models.CharField(max_length=20,blank=True)
    category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL,null=True,blank=True)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    status = models.CharField(choices=status_list,max_length=20)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = " Blogs"
        verbose_name = " Blogs" # 1 space



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=500, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
