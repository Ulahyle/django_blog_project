from django.shortcuts import render
from django.http import HttpResponse


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