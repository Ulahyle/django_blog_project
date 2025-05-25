from django.urls import path
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
