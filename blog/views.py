from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import PostAuthor, CustomPost
from  .forms import ContactUsForm

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

def search_view(request):
    if request.method == "POST":
        print(request.POST)
        form = searchForm(request.POST)
        if form.is_valid():
            tag_id = form.cleaned_data.get('tag_name')
            return HttpResponseRedirect(f'pages/tag_id/{tag_id}/')
        #return render(request,'home_layout/search.html', {"form": form})
    else:
        form = searchForm()
        return render(request,'home_layout/search.html', {"form": form})
    
def Contact_us_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('contact_success.html')
            return render(request,'contact_success.html')
    else:
        form = ContactUsForm()
        return render(request, 'contact_us.html',{'form':form})
