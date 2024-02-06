from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comentario

def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.img_url = '/Blog/img/thumbnails/' + post.img_url
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        conteudo = request.POST.get('conteudo')
        comentario = Comentario(nome=nome, email=email, conteudo=conteudo, post=post, likes=0) #associa o comentário com o post
        comentario.save() #salva o comentario no banco
        return redirect('post_detail', slug=post.slug) #Aqui serve para quando enviar o comentario ele 'reseta' a pgn

    post.img_url = '/Blog/img/thumbnails/' + post.img_url
    return render(request, 'post_details.html', {'post':post})
