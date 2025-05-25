from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import PostAuthor, CustomPost

from blog.forms import searchFormSubject,SearchFormInput

# Create your views here.

def home_page_view(request):
    tag_item = list()
    for item in CustomPost.objects.all():
        tag_item.append(item.tag)
    if request.method == "POST":
        form_Input = SearchFormInput(request.POST)
        form_subject = searchFormSubject(request.POST)
        if form_Input.is_valid() or form_subject.is_valid():
            input_id = form_Input.cleaned_data.get('custom_input')
            if form_subject.save().custom_field == 'tag_name':
                return HttpResponseRedirect(f'pages/tag_id/{input_id}/')
            if form_subject.save().custom_field == 'key_word':
                return HttpResponseRedirect(f'pages/key_word/{input_id}/')
            if form_subject.save().custom_field == 'title':
                return HttpResponseRedirect(f'pages/title/{input_id}/')
    else:
        form_Input = SearchFormInput()
        form_subject = searchFormSubject()
        context = {'form': form_Input,
                   'form_subject': form_subject,
                   'tag_item': set(tag_item)}
        return render(request, 'home_layout/home_home.html', context)
def post_model_view(request,tag_id):
    post_list = CustomPost.objects.filter(tag = tag_id)
    return render(request,'Pages/home_pages.html', {"post_list": post_list})

def key_word_view(request,input_id):
    post_list = CustomPost.objects.filter(description__icontains=input_id)
    return render(request, 'Pages/home_pages.html', {"post_list": post_list})

def title_view(request,input_id):
    post_list = CustomPost.objects.filter(title__icontains=input_id)
    return render(request, 'Pages/home_pages.html', {"post_list": post_list})
def search_view(request):
    if request.method == "POST":
        print(request.POST)
        form = searchFormSubject(request.POST)
        if form.is_valid():
            tag_id = form.cleaned_data.get('tag_name')
            return HttpResponseRedirect(f'pages/tag_id/{tag_id}/')
        #return render(request,'home_layout/search.html', {"form": form})
    else:
        form = SearchFormInput()
        return render(request,'home_layout/search.html', {"form": form})