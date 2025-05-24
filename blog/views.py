from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



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
