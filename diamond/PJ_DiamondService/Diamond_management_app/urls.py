# from django.urls import path
# from . import views

# urlpatterns = [
#     path('news/', views.news_view, name='news'),
#     path('add-news/', views.add_news, name='add_news'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.diamond_list, name='diamond_list'),
    path('diamond/add/', views.add_diamond, name='add_diamond'),
    path('diamond/delete/<int:diamond_id>/', views.delete_diamond, name='delete_diamond'),
]
