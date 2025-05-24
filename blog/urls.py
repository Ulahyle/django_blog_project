from django.urls import path

from blog.views import set_theme_cookie , get_theme_cookie , delete_theme_cookie
from blog.views import track_viewed_posts , get_recent_views , empty_viewed_posts , track_keywords , get_recent_keywords , empty_keywords


urlpatterns = [
                       #cookies

    path('set_theme_cookie/<str:theme>/', set_theme_cookie, name="set_theme_cookie"),
    path('get_theme_cookie/' , get_theme_cookie , name="get_theme_cookie"),
    path("delete_theme_cookie/", delete_theme_cookie, name="delete_theme_cookie"),

                         #sessions

    path("track_viewed_posts/<int:post_id>/", track_viewed_posts, name="track_viewed_posts"),
    path("get_recent_views/", get_recent_views, name="get_recent_views"),
    path("clear_viewed_posts/", empty_viewed_posts, name="empty_viewed_posts"),


    path("track_keywords/<str:keyword>/", track_keywords, name="track_keywords"),
    path("get_recent_keywords/", get_recent_keywords, name="get_recent_keywords"),
    path("empty_keywords/" , empty_keywords , name="empty_keywords"),


]