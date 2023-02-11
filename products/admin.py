from django.contrib import admin
from .models import Favorite, Coupon, Category, Warranty, Product


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user', 'product')
    list_filter = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'discount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('discount',)


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'warranty', 'category', 'status', 'created_at')
    search_fields = ('title', 'description', 'material', 'price')
    list_filter = ('user', 'status', 'warranty', 'category',)


admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Product, ProductAdmin)
