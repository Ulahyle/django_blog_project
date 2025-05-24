from django.shortcuts import render
from blog.models import PostAuthor, CustomPost

from blog.forms import searchForm

# Create your views here.

def home_page_view(request):
    tag_item = list()
    for item in CustomPost.objects.all():
        tag_item.append(item.tag)
    return render(request, 'home_layout/home_home.html', {"tag_item": set(tag_item)})
def post_model_view(request,tag_id):
    post_list = CustomPost.objects.filter(tag = tag_id)
    return render(request,'Pages/home_pages.html', {"post_list": post_list})