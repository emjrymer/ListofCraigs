from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import generics


# Create your views here.
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from app.models import Category, UserProfile, City, Post, SubCategory
from app.serializers import CategorySerializer, SubCategorySerializer, PostSerializer


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login_view")


class MyAccountView(TemplateView):
    model = UserProfile
    template_name = 'userprofile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MyAccountView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user.id)
        return context


class CityListView(ListView):
    model = City


class CityCreateView(CreateView):
    model = City
    fields = ("city", )

    def form_valid(self, form):
        city_object = form.save(commit=False)
        city_object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("main_view")


class CategoryByCityDetailView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(city=self.kwargs.get('pk'))


class UserUpdateView(UpdateView):
    model = UserProfile


class SubCategoryView(ListView):

    def get_queryset(self):
        return SubCategory.objects.filter(category=self.kwargs['pk'])


class PostView(ListView):

    def get_queryset(self):
        return Post.objects.filter(subcategory=self.kwargs.get('pk'))


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'subcategory', 'photo')

    def form_valid(self, form):
        post_object = form.save(commit=False)
        post_object.user = self.request.user
        post_object.subcategory = SubCategory.objects.get(pk=self.kwargs.get("sub_id"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class PostDetailView(DetailView):
    model = Post


class SuccessPostView(TemplateView):
    template_name = 'success.html'


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class PostBySubListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(subcategory=self.kwargs['pk'])


class PostByCatListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(subcategory__category=self.kwargs['pk'])


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, )

    def queryset(self):
        return Post.objects.filter(user_id=self.request.user)
