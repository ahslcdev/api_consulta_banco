from django.urls import path

from apps.core.views import index, login_page, logout_page

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name='logout'),
]