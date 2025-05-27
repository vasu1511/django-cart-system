from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import (
    CartListCreateView, CartUpdateDeleteView,
    ClearCartView, CartTotalView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('cart/', CartListCreateView.as_view(), name='cart_list_create'),
    path('cart/<int:item_id>/', CartUpdateDeleteView.as_view(), name='cart_update_delete'),
    path('cart/clear/', ClearCartView.as_view(), name='cart_clear'),
    path('cart/total/', CartTotalView.as_view(), name='cart_total'),
]
