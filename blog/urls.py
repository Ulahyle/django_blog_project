from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views
from blog.views import (
    set_theme_cookie, get_theme_cookie, delete_theme_cookie,
    track_viewed_posts, get_recent_views, empty_viewed_posts,
    track_keywords, get_recent_keywords, empty_keywords,
    track_ratings, get_recent_ratings, empty_ratings,
    check_request_user, check_request_user_template,
    custom_login, custom_logout, custom_sign_up
)

urlpatterns = [
    # Core Views
    path('', views.home_page_view, name='home'),
    path('pages/tag_id/<str:tag_id>/', views.post_model_view),
    path('search/pages/tag_id/<str:tag_id>/', views.post_model_view),
    path('pages/tag_id/<str:tag_id>/', views.post_model_view),
    path('pages/key_word/<str:input_id>/', views.key_word_view),
    path('pages/title/<str:input_id>/', views.title_view),
    # ------------------------------------------------------------------------
    path('topic/', views.topic_view, name='topic'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('write/', views.write_view, name='write'),
    path('signup/', custom_sign_up, name='signup'),
    path('login/signup/', custom_sign_up),
    path('login/', custom_login, name='login_page'),
    path('logout/', custom_logout, name='logout_page'),
    path('edit/<str:tag_id>/', views.edit_post_view, name='edit'),
    path('report/<str:tag_id>/', views.report_post_view, name='report'),


    # Cookies
    path('set_theme_cookie/<str:theme>/', set_theme_cookie, name="set_theme_cookie"),
    path('get_theme_cookie/', get_theme_cookie, name="get_theme_cookie"),
    path("delete_theme_cookie/", delete_theme_cookie, name="delete_theme_cookie"),

    # Sessions
    path("track_viewed_posts/<int:post_id>/", track_viewed_posts, name="track_viewed_posts"),
    path("get_recent_views/", get_recent_views, name="get_recent_views"),
    path("empty_viewed_posts/", empty_viewed_posts, name="empty_viewed_posts"),
    
    path("track_keywords/<str:keyword>/", track_keywords, name="track_keywords"),
    path("get_recent_keywords/", get_recent_keywords, name="get_recent_keywords"),
    path("empty_keywords/", empty_keywords, name="empty_keywords"),
    
    path("track_ratings/<int:post_id>/<int:rating>/", track_ratings, name="track_rating"),
    path("get_recent_ratings/", get_recent_ratings, name="get_recent_ratings"),
    path("empty_ratings/", empty_ratings, name="empty_ratings"),

    # User Authentication
    path('check_request/', check_request_user),
    path('check_request_templates/', check_request_user_template),



]
