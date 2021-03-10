from django.urls import path

from bargain.views import show_purchases, create_purchase, remove_purchase

urlpatterns = (
    path('<int:pk>/', show_purchases, name='purchases'),
    path('<int:user_pk>/<int:product_pk>', remove_purchase, name='remove purchase'),
    path('add_purchase/<int:user_pk>/<int:watch_pk>', create_purchase, name='create purchase'),
)
