from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,BlogCategory,Comment
from django.contrib import messages
from .forms import CommentForm
from django.db.models import Q


# Create your views here.
def blogs(request ,category_slug = None):
    categories=None
    
    if category_slug !=None:
        categories = get_object_or_404(BlogCategory, slug=category_slug)
        blogs_data = Blog.objects.filter(category=categories,status ='Published').order_by('-updated_at') 
        blog_category = BlogCategory.objects.all()
       
       
    else:
        blogs_data = Blog.objects.filter(status ='Published').order_by('-updated_at') 
        blog_category = BlogCategory.objects.all()

    return render(request,'blogs/blogs.html',{'blogs_data':blogs_data,'blog_category':blog_category})


def singleBlog(request,pk):
    blog = Blog.objects.filter(pk = pk).first()
    blogs_data = Blog.objects.filter(status ='Published').order_by('-updated_at')
    blog_category = BlogCategory.objects.all()
    # blog_content = BlogContent.objects.filter(blog = blog)
    comments = Comment.objects.filter(blog_id= blog.id, status=True)
    return render(request,'blogs/singleBlog.html',{'blog':blog,'blog_category':blog_category,'blogs_data':blogs_data,'comments':comments})



def submit_comment(request, blog_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = blog_id
            data.save()
            messages.success(request, 'Thank you! Your comments has been submitted.')
            return redirect(url)
        
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs=Blog.objects.order_by('-created_date').filter(Q(content__icontains=keyword) | Q(title__icontains=keyword))
            
    context={
        'blogs': blogs,
    }
    return render(request,'blogs/blogs.html' , context)
            