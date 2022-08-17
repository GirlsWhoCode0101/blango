import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
#  from django.views.decorators.cache import cache_page
#  from django.views.decorators.vary import vary_on_cookie

logger = logging.getLogger(__name__)


#  @cache_page(300)
#  @vary_on_cookie
def index_view(request):
    #  from django.http import HttpResponse
    #  return HttpResponse(str(request.user).encode("ascii"))
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")  #  select_rel is like a join in SQL
    logger.debug("Got %d posts", len(posts))
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
                logger.info("Created comment on Post %d for user %s", post.pk, request.user)
                return redirect(request.path_info)  # this refreshes the page for the user to see their comment
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})

#  for DjDebugToolbar we need the IP adress Django sees
def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])