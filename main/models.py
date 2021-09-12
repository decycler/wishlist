from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	"""Таблица "Товаров"

	id
	Название товара
	Ссыдка на товар
	Цена товара
	Дата и время создания записи
	"""
	title = models.CharField(max_length=120)
	link = models.URLField()
	price = models.IntegerField()
	create_at = models.DateTimeField(
		auto_now_add=True,
		auto_created=True
	)

	def __str__(self):
		return self.title

class WishList(models.Model):
	"""
	id - создаст django
	owner - владелец
	products - ManyToMany
	is_hidden - bool

	"""
	title = models.CharField(max_length=120)
	product = models.ManyToManyField(Product)
	is_hidden = models.BooleanField(default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title



