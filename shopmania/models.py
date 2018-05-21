from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 120, db_index = True)
    slug = models.SlugField(max_length = 120, unique = True, db_index = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def  get_absolute_url(self):
        return reverse('shopmania:product_list_by_category', args= [self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name= 'products', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, db_index = True)
    company = models.CharField(max_length = 100)
    slug = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    available = models.BooleanField(default = True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image_1 = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shopmania:product_detail', args=[self.id, self.slug])
