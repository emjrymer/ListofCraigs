import django
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app.views import MainView, CreateUserView, MyAccountView, CityCreateView, CityListView, CategoryByCityDetailView, SubCategoryView, PostView, PostCreateView, SuccessPostView, \
    PostDetailView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, SubCategoryListCreateAPIView, \
    SubCategoryRetrieveUpdateDestroyAPIView, PostRetrieveUpdateDestroyAPIView, \
    PostBySubListCreateAPIView, PostByCatListCreateAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainView.as_view(), name="main_view"),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^login/$', auth_views.login, name='login_view'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout_view'),
    url(r'^my_account/(?P<pk>\d+)/$', MyAccountView.as_view(), name='my_account_view'),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
    url(r'^successfully_posted/', SuccessPostView.as_view(), name='success'),
    url(r'^create_city/', CityCreateView.as_view(), name='city_create_view'),
    url(r'^city_list/$', CityListView.as_view(), name="city_list_view"),
    url(r'^categories_by_city/(?P<pk>\d+)/$', CategoryByCityDetailView.as_view(), name="category_by_city_detail_view"),
    url(r'^subcategory/(?P<pk>\d+)/$', SubCategoryView.as_view(), name='subcategory_view'),
    url(r'^post_by_sub/(?P<pk>\d+)/$', PostView.as_view(), name="post_view"),
    url(r'^post_create/(?P<sub_id>\d+)/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^post_detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_view'),
    url(r'^api/categories/$', CategoryListCreateAPIView.as_view()),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/subcategories/$', SubCategoryListCreateAPIView.as_view()),
    url(r'^api/subcategories/(?P<pk>\d+)/$', SubCategoryRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/subcategories/(?P<pk>\d+)/post/$', PostBySubListCreateAPIView.as_view()),
    url(r'^api/categories/(?P<pk>\d+)/post/$', PostByCatListCreateAPIView.as_view()),
    url(r'^api/posts/(?P<pk>\d+)/$', PostRetrieveUpdateDestroyAPIView.as_view()),
]
