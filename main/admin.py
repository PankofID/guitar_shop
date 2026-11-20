from django.contrib import admin

from .models import Category, Brand, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'brand', 'title', 'slug', 'article', 'count', 'price', 'available', 'created_at', 'updated_at']
    search_fields = ['title', 'article']
    list_filter = ['category', 'brand', 'available']
    list_editable = ['price', 'available', 'count']
    readonly_fields = ['created_at', 'updated_at', 'article']
    date_hierarchy = 'created_at'

    prepopulated_fields = {'slug': ('title',)}
