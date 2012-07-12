"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    lis=[]
    for e in post_list:
    	lis.append(e.title)
    return HttpResponse(lis)

def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if(showComments):
    	out='<h1>'+post.title+'</h1>'+'<br>'+post.body[:100]+'<br>'+post.body[100:200]
    else:
    	out='<h1>'+post.title+'<br>'+'</h1>'
    return HttpResponse(out)
def post_search(request, term):
    pass

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
