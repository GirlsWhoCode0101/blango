from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from blog.models import Post

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author, current_user=None):
# ---or as tag with context and no arguments:
#  @register.simple_tag(takes_context=True)
#  def author_details_tag(context):
#    request = context["request"]
#    current_user = request.user
#    post = context["post"]
#    author = post.author
  if not isinstance(author, user_model):
    return ""
  
  if author == current_user:
        return (format_html(f'<strong>me</strong>'))

  if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
  else:
        name = escape(f"{author.username}")

  if author.email:
        email = author.email
        prefix = f'<a href="mailto:{email}">'
        suffix = "</a>"
  else:
        prefix = ""
        suffix = ""

  return mark_safe(f"{prefix}{name}{suffix}")


#------------simple tag ----------------------
@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return format_html('</div>')


#---------inclusion tag -----------
@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
      posts = Post.objects.exclude(pk=post.pk)[:5]
      return {"title": "Recent Posts", "posts": posts}