from django.contrib import admin

# Register your models here.
from app.models import Category, SubCategory, UserProfile, City, Post

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Post)
