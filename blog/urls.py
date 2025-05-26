from django.urls import path
from .views import Contact_us_view
from blog import views

urlpatterns = [
    path('pages/tag_id/<str:tag_id>/',views.post_model_view),
    path('home/',views.home_page_view),
    path('search/',views.search_view),
    path('search/pages/tag_id/<str:tag_id>/',views.post_model_view),
    path('contact/', Contact_us_view,name='contact_us'),
]