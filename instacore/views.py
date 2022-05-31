
from dataclasses import fields
from venv import create
from django.urls import reverse_lazy,reverse
from pyexpat import model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout


# from .forms import NewPostForm


# from comment.models import Comment
# from comment.forms import CommentForm

from django.urls import reverse
from .models import Profile



# Create your views here.
from .models import *
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('detail',args=[str(pk)]))


class homeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-pk']

class CretaePostView(CreateView):
    model=Post
    template_name='createpost.html'
    fields=['image','caption']
    success_url=reverse_lazy('home')

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    fields=['image','caption']
    success_url=reverse_lazy('home')

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    fields=['image','caption']
    success_url=reverse_lazy('home')

class PostsView(ListView):
    model=Post
    template_name='posts.html'
    ordering=['-pk']





class CreateReelView(CreateView):
    model=Reel
    template_name='create_reel.html'
    fields=['reel','caption']

class UpdateReelView(UpdateView):
    model=Reel
    template_name='update_reel.html'
    fields=['reel','caption']

class DeleteReelView(DeleteView):
    model=Reel
    template_name='delete_reel.html'
    fields=['reel','caption']

class ReelsView(ListView):
    model=Reel
    template_name='reels.html'
    ordering=['-pk']





class DetailsView(DetailView):
    model=Post
    template_name='detail.html'

    def get_context_data(self,*args, **kwargs):
        posts=Post.objects.all()
        context=super(DetailsView,self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
       
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
            context["posts"]=posts
            context['total_likes']=total_likes
            context["liked"]=liked
        return context

 


    

class Profileview(CreateView):
    model=Profile
    template_name='create_profile.html'
    fields=['user','name','bio','photo']
    success_url=reverse_lazy('home')
    


class ProfileEditView(UpdateView):
    model=Profile
    template_name='update_profile.html'
    fields=['name','bio','photo']
    success_url=reverse_lazy('home')



def follow(request,id,username):
    profile = Profile.objects.get(id=id)
    Login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        Login_profile.followings.remove(profile.user)
    else:
        profile.followers.add(request.user)
        Login_profile.followings.add(profile.user)
    return redirect(f'/search?username={username}')






def search(request):
    profile = Profile.objects.get(user=request.user)
    profileimage = profile.photo.url
    search = request.GET['username']
    profiles = Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles,'username':search,"profileimage":profileimage}
    return render(request,'search.html',context)



def ProfileView(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'profile_view.html',{'profile':profile})



