from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from blog.forms import LoginCustomForm , CustomUserCreationForm
from blog.models import Posts , CustomPost



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




#recomendation partttttttttttt




from django.shortcuts import render

def get_recommendations(request):

    viewed_posts = request.session.get("viewed_posts", [])
    keywords = request.session.get("keywords", [])
    ratings = request.session.get("ratings", {})

    print(f"Viewed Posts: {viewed_posts}")
    print(f"Keywords: {keywords}")
    print(f"Ratings: {ratings}")

    recommendations = []

    if viewed_posts:
        viewed_titles = list(Posts.objects.filter(id__in=viewed_posts).values_list("title", flat=True))
        if viewed_titles:
            category_recommendations = list(Posts.objects.filter(title__in=viewed_titles).exclude(id__in=viewed_posts)[:5])
            recommendations.extend(category_recommendations)

    if keywords:
        keyword_recommendations = list(CustomPost.objects.filter(tag__in=keywords).distinct()[:5])
        recommendations.extend(keyword_recommendations)


    if ratings:
        high_rated_posts = [post_id for post_id, rating in ratings.items() if rating >= 4]
        if high_rated_posts:
            rating_recommendations = list(CustomPost.objects.filter(id__in=high_rated_posts)[:5])
            recommendations.extend(rating_recommendations)


    recommendations = list(set(recommendations))[:5]

    return render(request, "index.html", {"recommendations": recommendations})




def get_keyword_based_recommendations(request):
    keywords = request.session.get("keywords", [])

    recommendations = CustomPost.objects.none()

    if keywords:
        recommendations = CustomPost.objects.filter(tags__name__in=keywords).distinct()[:5]

    return render(request, "index.html", {"recommendations": recommendations})


def get_rating_based_recommendations(request):
    ratings = request.session.get("ratings", {})

    recommendations = CustomPost.objects.none()

    if ratings:
        high_rated_posts = [post_id for post_id, rating in ratings.items() if rating >= 4]
        if high_rated_posts:
            recommendations = CustomPost.objects.filter(id__in=high_rated_posts)[:5]

    return render(request, "index.html", {"recommendations": recommendations})






def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, "post_detail.html", {"post": post})
