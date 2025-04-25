from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post
from .forms import PostForm

# List all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs/post_list.html', {'posts': posts})
    # return HttpResponse('ok')
    

# Create new post
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blogs/post_form.html', {'form': form})

# Update post
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blogs/post_form.html', {'form': form})

# Delete post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blogs/post_confirm_delete.html', {'post': post})
