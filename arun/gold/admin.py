from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Contact)
class CotactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message','mobile']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','category','subcategory']


@admin.register(slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product_name','username','price','image','idd','count','final_price']

@admin.register(user_address)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','name']

@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','idd','uname','time','desc']