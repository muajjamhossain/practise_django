from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post, Category
from .forms import PostForm, CategoryForm
from django.db.models import Q
# views.py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


from django.http import JsonResponse
from .utils import send_notification_to_all

# List all posts
def post_list(request):
    categories = Category.objects.all()
    # return HttpResponse(categories)
    category = Category.objects.get(id=1)
    catPost = category.posts.all()
    # Note: you used `related_name='posts'` in your model. So it is `posts.all()`, not `post_set.all()`

    query = request.GET.get('q')  # ✅ Get search input

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        posts = Post.objects.all()

    return render(request, 'blogs/post_list.html', {
        'posts': posts,
        'query': query,
        'categories ': categories,
        'catPost': catPost
    })

    

# Create new post
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        send_notification_to_all("New user registered!")
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





def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blogs/post_form.html', {'form': form})


def send_test_notification(request):
    message = "This is a test notification."
    send_notification_to_all(message)
    return HttpResponse("Test notification sent.")

def send_notification_to_all(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications_group",
        {
            "type": "send_notification",
            "message": message,
        }
    )
