from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name="index"),
    path("subscribe", views.subscribe, name='subscribe'),
    path('login',views.login, name='login'),
    path('', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]