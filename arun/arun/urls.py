"""arun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from gold.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='home'),
    path('about/',about,name = 'about'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('contact/',contact,name='contact'),
    path('show/', show),
    path('buy/<int:id>',buy,name='buy'),
    path('search', search),
    path('register',register,name='register'),
    path('cart/<int:id>/',user_cart,name='cart'),
    path('cart',cart_page,name='cart_page'),
    path('cart_remove/<int:id>/',cart_remove),
    path('cart_plus/<int:id>',cart_plus),
    path('cart_minus/<int:id>',cart_minus),
    path('changepass/',change_password,name='changepass'),
    path('buypage/',buypage,name='buypage'),
    path('remove_address/<int:id>/',remove_address,name='remove_address'),
    path('order_detail/<int:id>/',order_detail,name='order_detail'),
    path('pdf_detail/',pdf_detail,name='pdf_detail'),
    path('user_coment/<int:id>/',user_comment,name='user_coment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

