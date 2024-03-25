from django.core.validators import MaxValueValidator
from django.db import models

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    password = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name,self.phone_number}"





class Rating(models.Model):
    ratingId = models.AutoField(primary_key=True)
    productId = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    customerId = models.OneToOneField(Customer, on_delete=models.CASCADE, unique=True, null=True)



class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.categoryName}"

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    productName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(default=True)

    def __str__(self):
        return f"{self.productName}"



class Cart(models.Model):
    cartId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    customerId= models.ForeignKey(Customer, on_delete=models.CASCADE)

