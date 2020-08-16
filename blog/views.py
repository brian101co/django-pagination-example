from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def posts(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 5)
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    else:
        page = None
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
        page = 1
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        page = paginator.num_pages

    return render(request, 'blog_listing_page.html', {
                    'posts':posts, 
                    'page_range': paginator.page_range, 
                    'num_pages': paginator.num_pages,
                    'current_page': page})
  
