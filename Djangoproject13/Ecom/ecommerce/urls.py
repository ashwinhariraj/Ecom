from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('create/', views.create_product, name='create_product'),
]
