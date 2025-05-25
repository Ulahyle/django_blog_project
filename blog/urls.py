from django.urls import path
<<<<<<< HEAD
from blog import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('topic/', views.topic_view, name='topic'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('write/', views.write_view, name='write'),
    path('edit/<int:post_id>/', views.edit_post_view, name='edit'),
    path('report/<int:post_id>/', views.report_post_view, name='report'),
    #user_status
    path('check_request/' , views.check_request_user),
    path('check_request_templates/' , views.check_request_user_template),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/' , views.custom_sign_up, name='signup')  
]
=======

<<<<<<< HEAD
from blog import views

urlpatterns = [
    path('pages/tag_id/<str:tag_id>/',views.post_model_view),
    path('home/',views.home_page_view),
    path('search/',views.search_view),
    path('search/pages/tag_id/<str:tag_id>/',views.post_model_view),
    path('home/pages/tag_id/<str:tag_id>/',views.post_model_view),
    path('home/pages/key_word/<str:input_id>/',views.key_word_view),
    path('home/pages/title/<str:input_id>/',views.title_view),
]
=======
from blog.views import set_theme_cookie , get_theme_cookie , delete_theme_cookie

from blog.views import track_viewed_posts , get_recent_views , empty_viewed_posts , track_keywords , get_recent_keywords , empty_keywords

from blog.views import track_ratings, get_recent_ratings, empty_ratings

from blog.views import check_request_user , check_request_user_template , custom_login , custom_logout

from blog.views import custom_sign_up



urlpatterns = [
                       #cookies

    path('set_theme_cookie/<str:theme>/', set_theme_cookie, name="set_theme_cookie"),
    path('get_theme_cookie/' , get_theme_cookie , name="get_theme_cookie"),
    path("delete_theme_cookie/", delete_theme_cookie, name="delete_theme_cookie"),

                         #sessions

    path("track_viewed_posts/<int:post_id>/", track_viewed_posts, name="track_viewed_posts"),
    path("get_recent_views/", get_recent_views, name="get_recent_views"),
    path("empty_viewed_posts/", empty_viewed_posts, name="empty_viewed_posts"),


    path("track_keywords/<str:keyword>/", track_keywords, name="track_keywords"),
    path("get_recent_keywords/", get_recent_keywords, name="get_recent_keywords"),
    path("empty_keywords/" , empty_keywords , name="empty_keywords"),


    path("track_ratings/<int:post_id>/<int:rating>/", track_ratings, name="track_rating"),
    path("get_recent_ratings/", get_recent_ratings, name="get_recent_ratings"),
    path("empty_ratings/", empty_ratings, name="empty_ratings"),



                         #login/logout      

    path('check_request/' , check_request_user),
    path('check_request_templates/' , check_request_user_template),
    path('custom_login/' , custom_login , name = 'login_page'),
    path('custom_logout/' , custom_logout , name = 'logout') ,
    path('signup/' , custom_sign_up),                       





]

>>>>>>> feature/session-cookies
>>>>>>> bf03400009667bd65c29be642ef1afdf541c19fd
