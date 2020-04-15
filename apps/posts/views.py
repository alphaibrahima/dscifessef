from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm, PostForm, AnnonceForm,VolontariaForm
from .models import *
from django.urls import reverse


def PostView(request):
    post = Post.objects.filter(archive=False).order_by('-timestamp')
    latest = Annonce.objects.order_by('-timestamp')[0:3]
    context = {
        'last' : latest,
        'posts' : post,
    }
    return render(request,'blog/post.html', context)

def DetailView(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("details", kwargs={
                'id': post.pk
            }))
 
    context = {
        'form' : form,
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)
    
def PostCreation(request):
    title = "Creer un publication"
    form = PostForm(request.POST or None, request.FILES or None)
    author =  request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("details", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "blog/post_create.html", context)

def UpdateView(request, id):
    title = "Update"
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author =  request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("details", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title, 
        'form': form
    }
    return render(request, "blog/post_create.html", context)

def DeleteView(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("posts"))

def AnnonceView(request):
    annonce = Annonce.objects.filter(archive=False).order_by('-timestamp')
    context = {
        'posts' : annonce
    }
    return render(request,'blog/annonce.html', context)

def AnnonceCreation(request):
    title = "Creer une annonce"
    form = AnnonceForm(request.POST or None, request.FILES or None)
    author =  request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("details", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "blog/post_create.html", context)

def DetailAnnonceView(request, id):
    post = get_object_or_404(Annonce, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("details", kwargs={
                'id': post.pk
            }))
 
    context = {
        'form' : form,
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)

def UpdateAnnonceView(request, id):
    title = "Update"
    post = get_object_or_404(Annonce, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author =  request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("details", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title, 
        'form': form
    }
    return render(request, "blog/post_create.html", context)

def DeleteAnnonceView(request, id):
    post = get_object_or_404(Annonce, id=id)
    post.delete()
    return redirect(reverse("annonces"))


def VolontariaView(request):
    volontaria = Volontaria.objects.filter(archive=False).order_by('-timestamp')
    context = {
        'posts' : volontaria
    }
    return render(request,'blog/annonce.html', context)

def VolontariaViewCreation(request):
    title = "Creer Une Annonce Pour Avoir Des Volontaire"
    form = VolontariaForm(request.POST or None, request.FILES or None)
    author =  request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("details", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "blog/post_create.html", context)

def DetailVolontaireView(request, id):
    post = get_object_or_404(Volontaria, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("details", kwargs={
                'id': post.pk
            }))
 
    context = {
        'form' : form,
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)


def UpdateVolontaireView(request, id):
    title = "Update"
    post = get_object_or_404(Volontaria, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author =  request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("details", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title, 
        'form': form
    }
    return render(request, "blog/post_create.html", context)


def DeleteVolontaireView(request, id):
    post = get_object_or_404(Volontaria, id=id)
    post.delete()
    return redirect(reverse("volontaire"))