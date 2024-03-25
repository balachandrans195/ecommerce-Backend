from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CustomerAPIView, RatingListAPIView, RatingDetailAPIView, CategoryListAPIView, ProductListAPIView, \
    ProductDetailAPIView, CategoryDetailAPIView, CartDetailAPIView, CartListAPIView

urlpatterns = [
    path('customers/<int:customer_id>/', CustomerAPIView.as_view(), name='customer-detail'),
    path('customers/', CustomerAPIView.as_view(), name='customer-list'),

    path('ratings/', RatingListAPIView.as_view(), name='rating-list'),
    path('ratings/<int:rating_id>/', RatingDetailAPIView.as_view(), name='rating-detail'),

    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),

    path('customers/<int:customer_id>/cart/', CartListAPIView.as_view(), name='customer-cart-list'),
    path('cart/<int:cart_id>/', CartDetailAPIView.as_view(), name='cart-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

