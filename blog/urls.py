from django.urls import path

from blog.views import set_theme_cookie , get_theme_cookie , delete_theme_cookie

urlpatterns = [
    path('set_theme_cookie/<str:theme>/', set_theme_cookie, name="set_theme_cookie"),
    path('get_theme_cookie/' , get_theme_cookie , name="get_theme_cookie"),
    path("delete_theme_cookie/", delete_theme_cookie, name="delete_theme_cookie"),

]