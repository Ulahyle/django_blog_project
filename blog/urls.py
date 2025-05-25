from django.urls import path

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