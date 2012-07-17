"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



@csrf_exempt
def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))


               		


	

@csrf_exempt
def baseAfterLogin(request):
	username1= request.session['username']
        posts = Post.objects.all()
	t = loader.get_template('blog/baseAfterLogin.html')
	c = Context({'posts':posts },{'username1':username1 })
	return HttpResponse(t.render(c))

@csrf_exempt
def base(request):
       request.path='/blog'
       response = HttpResponseRedirect(request.path)
       response.delete_cookie('user_location')
       return response	



class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude=['post']
@csrf_exempt
def post_detail(request, id, showComments=False):
		wanted_post=Post.objects.get(pk=id)
		if request.method == 'POST':
			comment=Comment(post=wanted_post)	
			form = CommentForm(request.POST,instance=comment)
			if form.is_valid():
				form.save()
			else:
				print 'invalid'
			return HttpResponseRedirect(request.path)
		else:
			form = CommentForm()
		comments=Comment.objects.filter(post=wanted_post)
		t = loader.get_template('blog/post_detail.html')
		c = Context({'comments':comments,'form':form,'wanted_post':wanted_post })
		return HttpResponse(t.render(c))





@csrf_exempt
def home(request):

   if request.method == 'POST':
       if ((request.POST.keys()[0])=='username'):
           uname=request.POST.get('username')
           passw=request.POST.get('password')
           print str(uname)
           user=authenticate(username=uname,password=passw)
           if user is not None:
               if user.is_active:
                   print 'Correct username and password'
		   request.session['username']=uname
                   return render_to_response('blog/baseAfterLogin.html', {'logged_in': request.user.is_authenticated()})
               else:
                   print 'Account disabled'
		   
           else:
               print 'Incorrect password'   
               return render_to_response('blog/baseError.html')

   return render_to_response('blog/base.html',{})

@csrf_exempt
def edit_comment(request, id): 
    comments = Comment.objects.get(pk=id)
    if request.method == 'POST':
      # comment = Comment(post=post_item)
       form = CommentForm(request.POST,instance=comments)
       if form.is_valid():
            form.save()
	    return HttpResponseRedirect('/blog/posts/'+ str(comments.post.id))
    else:
	form = CommentForm(instance=comments)

    return render_to_response('blog/edit_comment.html',{'comments':comments,'form':form})


def post_search(request, term):
    posts =Post.objects.filter(title__contains= term)
    
    t = loader.get_template('blog/post_search.html')
    c = Context({'posts':posts,'term':term})

    return HttpResponse(t.render(c))


def post_search_linkedToTextBox(request, term):
	if request.method == 'POST2':
		if ((request.POST2.keys()[0])=='query'):
    			term1=request.POST2.get('query')
    			posts =Post.objects.filter(title__contains= term1)
    
    			t = loader.get_template('blog/post_search.html')
    			c = Context({'posts':posts,'term':term})

    			return HttpResponse(t.render(c)+term)
	else:
               print 'Cant Find Term'   
               return render_to_response('blog/baseAfterLogin.html')
		
   


