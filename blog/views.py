
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.forms import (
    LoginCustomForm, CustomUserCreationForm, Write,
    searchFormSubject, SearchFormInput,VoteByUserForm,ContactUsForm
)
from blog.models.models import CustomPost,Contactmodel,ReportPost

post_id_view = list()
keyword_search_view = list()
recent_rate_session = list()
def home_page_view(request):
    tag_item = list()
    for item in CustomPost.objects.all():
        tag_item.append(item.tag)
    if request.method == "POST":
        form_Input = SearchFormInput(request.POST)
        form_subject = searchFormSubject(request.POST)
        if form_Input.is_valid() or form_subject.is_valid():
            input_id = form_Input.cleaned_data.get('custom_input')
            if form_subject.save().Tag_field == 'tag_name':
                return HttpResponseRedirect(f'pages/tag_id/{input_id}/')
            if form_subject.save().Tag_field == 'key_word':
                return HttpResponseRedirect(f'pages/key_word/{input_id}/')
            if form_subject.save().Tag_field == 'title':
                return HttpResponseRedirect(f'pages/title/{input_id}/')
    else:
        form_Input = SearchFormInput()
        form_subject = searchFormSubject()
        context = {'form': form_Input,
                   'form_subject': form_subject,
                   'tag_item': set(tag_item),
                   'article' : CustomPost.objects.all}
        return render(request, 'home_layout/home_home.html', context)
def post_model_view(request,tag_id):
    post_list = CustomPost.objects.filter(tag = tag_id)
    for item in post_list:
        post_id_view.append(item.id)
    if request.method == "POST":
        input_rate = VoteByUserForm(request.POST)
        if input_rate.is_valid():
            recent_post_rate = dict()
            recent_post_rate["post_id"] = input_rate.cleaned_data.get('id_field')
            recent_post_rate["post_rate"] = input_rate.cleaned_data.get('custom_field')
            recent_rate_session.append(recent_post_rate)
            print(input_rate.save().custom_field)
            print(input_rate.save().id_field)
            context = {
                'form': input_rate,
                "post_list": post_list
            }
            return render(request, 'home_layout/home_pages.html', context)
    else:
        input_rate = VoteByUserForm()
        context = {
            'form': input_rate,
            "post_list": post_list
        }
        return render(request, 'home_layout/home_pages.html', context)
def key_word_view(request,input_id):
    post_list = CustomPost.objects.filter(description__icontains=input_id)
    keyword_search_view.append(input_id)
    return render(request, 'Pages/templates/home_layout/home_pages.html', {"post_list": post_list})

def title_view(request,input_id):
    post_list = CustomPost.objects.filter(title__icontains=input_id)
    return render(request, 'Pages/templates/home_layout/home_pages.html', {"post_list": post_list})
# --------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def write_view(request):
    print(request.user.first_name)
    if request.method == 'POST':
        form = Write(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            rate = form.cleaned_data['rate']
            tag = form.cleaned_data['tag']
            CustomPost.objects.create(title=title, description=description,rate = rate, tag = tag, authors = request.user)
            return render(request, 'page_view/write.html', {'form': form})
    else:
        form = Write()
        print(request.user.first_name)
    return render(request, 'page_view/write.html', {'form': form})

@login_required(login_url='/login/')
def edit_post_view(request, post_id):
    post = get_object_or_404(CustomPost, id=post_id)
    
    if post.authors != request.user:
        return HttpResponse("you don't have the permission to change this post!", status=403)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.save()
        return redirect('home')
    
    return render(request, 'page_view/edit.html', {'post': post})

@login_required(login_url='/login/')
def report_post_view(request, post_id):
    post = get_object_or_404(CustomPost, id=post_id)
    ReportPost.objects.create(post_title = CustomPost.objects.get(id=post_id).title,
                              reporter_id = request.user)
    return HttpResponse(f"the post {post.title} was reported by{request.user.username}")



#cookies

def set_theme_cookie(request, theme):
    # response = HttpResponse(f"Theme set to {theme}")
    response = redirect("cookie_session_handling")
    response.set_cookie("theme", theme, max_age=86400)
    return response



def get_theme_cookie(request):

    theme = request.COOKIES.get("theme", "light")
    return render(request , 'cookie_session/index.html' , {"theme" : theme})



def delete_theme_cookie(request):
    # response = HttpResponse("Theme is deleted succesfully!")
    response = redirect("cookie_session_handling")
    response.delete_cookie("theme")  
    return response


#sessions

def track_viewed_posts(request):
    if request.user.is_superuser:
        viewed_posts = request.session.get("viewed_posts", [])
        viewed_posts.insert(0, post_id_view)
        viewed_posts = viewed_posts[:5]
        request.session["viewed_posts"] = viewed_posts
        request.session.set_expiry(86400)
        return HttpResponse(f"Viewed posts: {viewed_posts}")
    else:
        return HttpResponse('YOU ONT HAVE ACCESS')

def get_recent_views(request):
    viewed_posts = request.session.get("viewed_posts", [])
    return render(request, "cookie_session/index.html", {"viewed_posts": viewed_posts})

def empty_viewed_posts(request):
    if request.user.is_superuser:
        del request.session['viewed_posts']
        post_id_view = list()
        # return HttpResponse("data deleted!")
        return redirect('cookie_session_handling')
    else:
        return HttpResponse('YOU ONT HAVE ACCESS')



def track_keywords(request):
    if request.user.is_superuser:
        keywords = request.session.get("keywords", [])
        keywords.insert(0, keyword_search_view)
        keywords = keywords[:5]
        request.session["keywords"] = keywords
        request.session.set_expiry(86400)
        return HttpResponse(f"Tracked Keywords: {keywords}")
    else:
        return HttpResponse('YOU ONT HAVE ACCESS')


def get_recent_keywords(request):
    keywords = request.session.get("keywords", [])
    return render(request, "cookie_session/index.html", {"keywords": keywords})


def empty_keywords(request):
    if request.user.is_superuser:
        del request.session['keywords']
        keyword_search_view = list()
        # return HttpResponse("data deleted!")
        return redirect ('cookie_session_handling')
    else:
        return HttpResponse('YOU ONT HAVE ACCESS')


def track_ratings(request):
    if request.user.is_superuser:
        ratings = request.session.get("ratings", {})
        print(recent_rate_session)
        request.session["ratings"] = recent_rate_session
        request.session.set_expiry(86400)
        # return redirect("get_recent_ratings")
        return HttpResponse(f"Tracked Ratings: {ratings}")
    else:
        return HttpResponse('YOU ONT HAVE ACCESS')


def get_recent_ratings(request):
    ratings = request.session.get("ratings", {})
    return render(request, "cookie_session/index.html", {"ratings": ratings})

def empty_ratings(request):
    if request.user.is_superuser:
        del request.session["ratings"]
        recent_rate_session = list()
        return redirect("cookie_session_handling")

    else:
        return HttpResponse('YOU ONT HAVE ACCESS')


def custom_login(request):
    if request.method == 'POST':
        form = LoginCustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request,
                username=username,
                password=password
                )
            if user:
                login(request, user)
                context = {'form': form, 'custom_message': f'welcome {user.username}'}
                return render(request, 'custom_login.html', context=context)
            else:
                context = {'form': form, 'custom_message': 'Please sign uo first!'}
                return redirect('signup/')
        else:
            context = {'form': form, 'custom_message': 'wrong form!'}
        return render(request, 'custom_login.html', context=context)

    form = LoginCustomForm()
    context = {'form': form}
    return render(request, 'custom_login.html', context=context)



def custom_logout(request):
    logout(request)
    return redirect('login_page')



def custom_sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = CustomUserCreationForm()
    return render(request , 'custom_signup.html' , {'form':form})

def custom_contactus(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            #contact_form.save()
            Contactmodel.objects.create(name=contact_form.cleaned_data.get('name'),
                                     email=contact_form.cleaned_data.get('email'),
                                     subject=contact_form.cleaned_data.get('subject'),
                                     message=contact_form.cleaned_data.get('message'))
        return render(request, 'ContactUs/contactus_.html', {'form': contact_form})
    else:
        contact_form = ContactUsForm()
        return render(request, 'ContactUs/contactus_.html', {'form': contact_form})





