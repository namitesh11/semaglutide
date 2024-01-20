from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
 
    path('',views.blogs,name="blogs"),
    path('<slug:category_slug>/',blogs , name='blogs_by_category'),
    path('singleBlog/<int:pk>/',singleBlog,name="singleBlog"),
    path('search/', views.search, name='search'),
    path('submit_comment/<int:blog_id>/', views.submit_comment, name='submit_comment'),
    
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)