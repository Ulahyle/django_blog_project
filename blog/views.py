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

def custom_login(request):
    if request.method == 'POST':
        form = LoginCustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
            request=request,
            username=username,
            password=password,
            )

            if user:
                login(request, user)
                return redirect('home')
            else:
                context = {'form': form, 'custom_message': 'wrong data!'}
        else:
            context = {'form': form, 'custom_message': 'wrong form!'}
        return render(request, 'user_status/custom_login.html', context=context)

    form = LoginCustomForm()
    context = {'form': form}
    return render(request, 'user_status/custom_login.html', context=context)

def custom_logout(request):
    logout(request)
    return redirect('login')

def custom_sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request , 'user_status/custom_signup.html' , {'form':form})