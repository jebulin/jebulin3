from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('', home, name='home'),
    path('user/', userPage, name='user'),

    path('account/', accountSettings, name='account'),

    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),

    path('inlineForm/<str:pk>', orderForm, name='orderCreate'),
    path('order_create/<str:pk>/', updateOrder, name='updateOrder'),
    path('delete_order/<str:pk>/', deleteOrder, name='deleteOrder'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
