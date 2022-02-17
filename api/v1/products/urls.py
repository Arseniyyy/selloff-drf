from django.urls import path, include

from v1.products import views


app_name = 'v1.products'
urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='latest_products'),
    path('search/', views.search),
    path('<slug:category_slug>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
]
