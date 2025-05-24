from django.urls import path

from blog import views

urlpatterns = [
    path('pages/tag_id/<str:tag_id>/',views.post_model_view),
    path('home/',views.home_page_view),
]