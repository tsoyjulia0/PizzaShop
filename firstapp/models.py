from django.db import models

# Create your models here.

class PizzaShop(models.Model):
    name = models.CharField(max_length=50, verbose_name='PizzaShop')
    description = models.TextField(verbose_name='Description')
    rating = models.FloatField(default=0, verbose_name='Rating')
    url = models.URLField(verbose_name='Internet_address')

    class Meta:
        verbose_name='PizzaShop'
        verbose_name_plural='pizzashops'

    # displays the name of object
    def __str__(self):
        return self.name

class Pizza(models.Model):
    # what happens if we delete from db
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='PizzaName')
    short_description = models.CharField(max_length=30, verbose_name='ShortDesc')
    price = models.IntegerField(default=0, verbose_name='Price')
    photo = models.ImageField('Photo', upload_to='firstapp/photos', default='', blank=True)

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'pizzas'
        # sorting by name
        ordering = ['name']

    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, verbose_name='Pizza', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Name')
    phone = models.CharField(max_length=30, verbose_name='Phone number')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
