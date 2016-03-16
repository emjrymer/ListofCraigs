from django.db import models


class SubCategoryManager(models.Manager):

    def get_subcategories_by_category(self, category):
        return self.filter(category=category)


class City(models.Model):
    user = models.ForeignKey("auth.User")
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = "Cities"


class Category(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)

    objects = SubCategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SubCategories"


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")


class Post(models.Model):
    subcategory = models.ForeignKey(SubCategory)
    title = models.CharField(max_length=30)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User")
    photo = models.ImageField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-time_created"]
