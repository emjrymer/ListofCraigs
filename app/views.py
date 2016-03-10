from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from app.forms import NewUserCreationForm
from app.models import Category, UserProfile, City, Post


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CreateUserView(CreateView):
    model = User
    form_class = NewUserCreationForm

    def get_success_url(self):
        return reverse("login_view")


class MyAccountView(DetailView):
    model = UserProfile


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


class PostingDetailView(DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(subcategory__category__city=City.objects.filter(user=self.request.user))


class CategoryByCityDetailView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(city=self.kwargs.get('pk'))


'''class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'subcategory')

    @property
    def subcategory(self):
        return Subcategory.objects.get(pk=self.kwargs.get('subcat_id')

    def get_context_data()
        context =
        context['sub
        return context
class CategoryListView(ListView):
    model = Category


class SubCategoryView(DetailView):
    pass'''