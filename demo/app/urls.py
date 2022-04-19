from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('sign-up/', views.sign_up, name='sign_up'),

    # User
    path('user/', views.user_index, name='user_index'),

    path('about/', views.about, name='about'),
    path('category-detail/', views.category_detail, name='category_detail'),
    path('product-detail/', views.product_detail, name='product_detail'),
]
