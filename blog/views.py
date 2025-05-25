<<<<<<< HEAD
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from blog.forms import LoginCustomForm, CustomUserCreationForm, Write
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from blog.models import Posts


def home_view(request):
    return render(request, 'page_view/home.html')

def topic_view(request):
    posts = Posts.objects.all()
    return render(request, 'page_view/topic.html', {'posts': posts})

def post_view(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, 'page_view/post.html', {'post': post})

@login_required(login_url='/login/')
def write_view(request):
    if request.method == 'POST':
        form = Write(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Posts.objects.create(title=title, description=description, wrote_by=request.user)
            return redirect('/home/')
    else:
        form = Write()
    return render(request, 'page_view/write.html', {'form': form})

@login_required(login_url='/login/')
def edit_post_view(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    
    if post.wrote_by != request.user:
        return HttpResponse("you don't have the permission to change this post!", status=403)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.save()
        return redirect('home')
    
    return render(request, 'page_view/edit.html', {'post': post})

@login_required(login_url='/login/')
def report_post_view(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return HttpResponse(f"the post {post.title} was reported by{request.user.username}")

#user_status
def check_request_user(request):
    return HttpResponse (f'{request.user} - {request.user.is_authenticated}')

def check_request_user_template(request):
    return render(request , 'user_status/check_user_request.html')
=======
<<<<<<< HEAD
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
=======
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from blog.forms import LoginCustomForm , CustomUserCreationForm

# Create your views here.


                        #cookies

def set_theme_cookie(request, theme):
    # response = HttpResponse(f"Theme set to {theme}")
    response = redirect("get_theme_cookie")
    response.set_cookie("theme", theme, max_age=86400)
    return response


def get_theme_cookie(request):
    theme = request.COOKIES.get("theme", "light")
    return render(request , 'index.html' , {"theme" : theme})



def delete_theme_cookie(request):
    # response = HttpResponse("Theme is deleted succesfully!")
    response = redirect("get_theme_cookie")
    response.delete_cookie("theme")  
    return response


                         #sessions

def track_viewed_posts(request, post_id):
    viewed_posts = request.session.get("viewed_posts", [])
    viewed_posts.insert(0, post_id)
    viewed_posts = viewed_posts[:5]
    request.session["viewed_posts"] = viewed_posts
    request.session.set_expiry(86400)
    return HttpResponse(f"Viewed posts: {viewed_posts}")



def get_recent_views(request):
    viewed_posts = request.session.get("viewed_posts", [])
    return render(request, "index.html", {"viewed_posts": viewed_posts})



def empty_viewed_posts(request):
    del request.session['viewed_posts']
    # return HttpResponse("data deleted!")
    return redirect('get_recent_views')



def track_keywords(request, keyword):
    keywords = request.session.get("keywords", [])
    keywords.insert(0, keyword)
    keywords = keywords[:5]
    request.session["keywords"] = keywords
    request.session.set_expiry(86400)
    return HttpResponse(f"Tracked Keywords: {keywords}")



def get_recent_keywords(request):
    keywords = request.session.get("keywords", [])
    return render(request, "index.html", {"keywords": keywords})


def empty_keywords(request):
    del request.session['keywords']
    # return HttpResponse("data deleted!")
    return redirect ('get_recent_keywords')



def track_ratings(request, post_id, rating):


    if rating < 0 or rating > 5:
        return HttpResponse("Invalid rating! please give a rating between 1 and 5.", status=400)

    ratings = request.session.get("ratings", {})
    ratings[str(post_id)] = rating
    request.session["ratings"] = ratings
    request.session.set_expiry(86400)
    # return redirect("get_recent_ratings")
    return HttpResponse(f"Tracked Ratings: {ratings}")



def get_recent_ratings(request):
    ratings = request.session.get("ratings", {})
    return render(request, "index.html", {"ratings": ratings})

def empty_ratings(request):
    del request.session["ratings"]
    return redirect("get_recent_ratings")




                             #login

def check_request_user(request):
    return HttpResponse (f'{request.user} - {request.user.is_authenticated}')



def check_request_user_template(request):
    return render(request , 'check_request_user.html')


>>>>>>> bf03400009667bd65c29be642ef1afdf541c19fd

def custom_login(request):
    if request.method == 'POST':
        form = LoginCustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
<<<<<<< HEAD
            request=request,
            username=username,
            password=password,
            )

            if user:
                login(request, user)
                return redirect('home')
=======
                request=request,
                username=username,
                password=password
                )
            if user:
                login(request, user)
                context = {'form': form, 'custom_message': f'welcome {user.username}'}
>>>>>>> bf03400009667bd65c29be642ef1afdf541c19fd
            else:
                context = {'form': form, 'custom_message': 'wrong data!'}
        else:
            context = {'form': form, 'custom_message': 'wrong form!'}
<<<<<<< HEAD
        return render(request, 'user_status/custom_login.html', context=context)

    form = LoginCustomForm()
    context = {'form': form}
    return render(request, 'user_status/custom_login.html', context=context)

def custom_logout(request):
    logout(request)
    return redirect('login')
=======
        return render(request, 'custom_login.html', context=context)

    form = LoginCustomForm()
    context = {'form': form}
    return render(request, 'custom_login.html', context=context)



def custom_logout(request):
    logout(request)
    return redirect('login_page')


>>>>>>> bf03400009667bd65c29be642ef1afdf541c19fd

def custom_sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request , 'user_status/custom_signup.html' , {'form':form})
=======
            return redirect('login_page')
    else:
        form = CustomUserCreationForm()
    return render(request , 'custom_signup.html' , {'form':form})




>>>>>>> feature/session-cookies
>>>>>>> bf03400009667bd65c29be642ef1afdf541c19fd
