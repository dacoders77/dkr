from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # Show name in admin panel. Not shown by default
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    # Show name in admin panel. Not shown by default
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    day_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)  # Many to many rel

    # Show name in admin panel. Not shown by default
    def __str__(self):
        return self.name

class Order(models.Model):
    # Status chices?
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) # Should be 1 to many rel. Keep the order if customer is deleted
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS) # choices - for a dropdown menu when new item created

    # Show name in admin panel. Not shown by default
    def __str__(self):
        return str(self.product.name)





