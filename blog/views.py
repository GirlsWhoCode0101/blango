from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm

def index_view(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)  # prevents from writing to database
                comment.content_object = post
                comment.creator = request.user
                comment.save() # now attributes are set and we can save
                return redirect(request.path_info)  # this refreshes the page for the user to see their comment
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})

