from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


def post_main(request) :
    posts = Post.objects.order_by('-pk')
    
    return render(request, 'blog/post_main.html', {'post': posts[0:3]})

def post_details(request, pk) :#시험
    posts = get_object_or_404(Post, pk=pk)#시험
    return render(request, 'blog/post_details.html', {'post': posts})

def post_folio(request) :
    name = request.GET.get('s', '')
    posts = Post.objects.filter(author__username=name)
    return render(request, 'blog/post_folio.html', {'post': posts, 'name':name})

@login_required
def post_new(request) :
    if request.method == "POST" :
        form = PostForm(request.POST, request.FILES)
        #form = PostForm()#시험
        if form.is_valid() : #폼유효성
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, pk=post.pk)
    else :
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

# Create your views here.
