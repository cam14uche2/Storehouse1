from turtle import setundobuffer
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})
    
    
    

    



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send email
        send_mail(
        name , # subject
        message , # message
        email  , # from email
        ['cam14uche@gmail.com']  , # To email



        )
        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})
    

def about(request):
    return render(request, 'about.html')    

# def LikeView(request, pk):
    #post = get_object_or_404(Post, id=request.POST.get('post_id'))
   # post.likes.add(request.user)
   # return HttpResponseRedirect(reverse('writeup-detail', args=[str(pk)]))
        

        

class HomeView(ListView):
    model =Post
    template_name = 'home.html'
    ordering = ['-id']
    ordering = ['-post_date']

class WriteupDetailView(DetailView):
    model =Post
    template_name = 'writeup_details.html'

    
        
        



class AddPostView(CreateView):
    model = Post
    form_class =PostForm
    template_name = 'add_post.html' 
    #fields = '__all__'  
    #fields = ('title', 'author', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class =PostForm
    template_name = 'add_category.html' 
    fields = '__all__'  
   # fields = ('title', 'author', 'body')
        
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'body'] 
            


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
        