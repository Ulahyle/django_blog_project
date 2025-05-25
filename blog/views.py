from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from blog.forms import LoginCustomForm , CustomUserCreationForm

# Create your views here.


                        #cookies

def set_theme_cookie(request, theme):
    response = HttpResponse(f"Theme set to {theme}")
    response.set_cookie("theme", theme, max_age=86400)
    return response


def get_theme_cookie(request):
    theme = request.COOKIES.get("theme", "light")
    return render(request , 'index.html' , {"theme" : theme})



def delete_theme_cookie(request):
    response = HttpResponse("Theme is deleted succesfully!")
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
    return HttpResponse("data deleted!")



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
    return HttpResponse("data deleted!")





                             #login

def check_request_user(request):
    return HttpResponse (f'{request.user} - {request.user.is_authenticated}')



def check_request_user_template(request):
    return render(request , 'check_request_user.html')



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
            else:
                context = {'form': form, 'custom_message': 'wrong data!'}
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

