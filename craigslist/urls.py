from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app.views import MainView, CreateUserView, MyAccountView, CityCreateView, CityListView, CategoryByCityDetailView, SubCategoryView, PostView, ContactSellerView, PostCreateView, SuccessPostView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainView.as_view(), name="main_view"),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^login/$', auth_views.login, name='login_view'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout_view'),
    url(r'^my_account/(?P<pk>\d+)/$', MyAccountView.as_view(), name='my_account_view'),
    url(r'^which_city/$', CityListView.as_view(), name="city_list_view"),
    url(r'^categories_by_city/(?P<pk>\d+)/$', CategoryByCityDetailView.as_view(), name="category_by_city_detail_view"),
    url(r'^create_city/', CityCreateView.as_view(), name='city_create_view'),
    url(r'^media/(?P<path>.*)', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    url(r'^subcategory/(?P<pk>\d+)/$', SubCategoryView.as_view(), name='subcategory_view'),
    url(r'^post_by_sub/(?P<pk>\d+)/$', PostView.as_view(), name="post_view"),
    #url(r'^contact_seller/(?P<pk>\d+)/$', ContactSellerView.as_view(), name="contact_seller"),
    url(r'^post_create/(?P<pk>\d+)/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^successfully_posted/', SuccessPostView.as_view(), name='success')
]
