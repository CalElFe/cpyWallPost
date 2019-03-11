from django.urls import path

from api import views

urlpatterns = [
    path('cpyPosts/view/<int:id>/', views.post_request),
    path('cpyPosts/add/', views.post_add),
    path('cpyPosts/edit/<int:id>/', views.post_edit),
    path('cpyPosts/del/<int:id>/', views.post_del),
    path('cpyPosts/qr/<int:id>/', views.post_get_QR),
]