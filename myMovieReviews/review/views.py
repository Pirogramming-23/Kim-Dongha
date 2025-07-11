from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def review_main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'review_main.html', {'posts': posts})

def review_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    hours = post.runningtime // 60
    minutes = post.runningtime % 60

    running_display = ""
    if hours:
        running_display += f"{hours}시간 "
    if minutes:
        running_display += f"{minutes}분"

    return render(request, 'review_detail.html', {
        'post': post,
        'running_display': running_display.strip()
    })

def review_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('review_main')
    else:
        form = PostForm()
    return render(request, 'review_edit.html', {'form': form})

def review_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('review_main')
    else:
        form = PostForm(instance=post)
    return render(request, 'review_edit.html', {'form': form})

def review_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('review_main')