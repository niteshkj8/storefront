from django.db import models

# Create your models here.

class Promotion(models.Model):
    descirption = models.CharField(max_length=255)
    discount= models.FloatField()
    featured_product= models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Collection(models.Model):
    title= models.CharField(max_length=255)

class Product(models.Model):
    title= models.CharField(max_length=255)
    slug= models.SlugField(default='-')
    description= models.TextField
    price= models.DecimalField(max_digits=6,decimal_places=2)
    inventory= models.IntegerField
    last_update= models.DateTimeField(auto_now=True)
    collection= models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion= models.ManyToManyField(Promotion)
    
class Customers(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    phone= models.CharField(max_length=20)
    birth_date= models.DateField(null=True)
    
class Order(models.Model):
    STATUS_PENDING= 'P'
    STATUS_COMPLETE= 'C'
    STATUS_FAILED= 'F'
    
    PAYMENT_CONFIRM= [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETE, 'Complete'),
        (STATUS_FAILED, 'Failed')
    ]
    
    placed_at= models.DateTimeField(auto_now_add=True)
    payment_status= models.CharField(max_length=1, choices=PAYMENT_CONFIRM, default=STATUS_PENDING)
    customer= models.ForeignKey(Customers, on_delete=models.PROTECT)
    
class Address(models.Model):
    street= models.CharField(max_length=255)
    city= models.CharField(max_length=25)
    customer= models.OneToOneField(Customers, on_delete=models.CASCADE, primary_key=True)
    
class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.PROTECT)
    product= models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity= models.PositiveSmallIntegerField()
    unit_price= models.DecimalField(max_digits=10, decimal_places=2)
    
class Cart(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveSmallIntegerField()


    
    
    
