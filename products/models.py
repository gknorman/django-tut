from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) # max_length=required
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000) # decimal_places, max_digits = required
    summary = models.TextField(blank=False, null=False) # default="this is cool" = optional, blank=True means it can be blank
    # blank=True, null=False, summary will not be bold and can be blank
    # blank=False, null=False summary will be bold and be required
    # BLANK has to do with how the field is RENDERED
    # NULL has to do with the DATABASE!!
    
    # Previously saved objects don't know about this field
    # If we want to add this new field to old objects, can set null=True or default=True
    # OR choose option 1 with makemigrations which creates a one-off
    # default for all of the previously created objects
    # will open a shell and you have to provide the one-off default, in this case is True
    featured = models.BooleanField()
    
    # if you don't run migrate, will crash the server!!
    # Always run migrate after makemigrations to update the database!
    
    
    
    
    
    
    
# In the shell, 

# from products.models import Product
# closer to absolute import ^^

# then
# Product.objects.all()
# Queries the current model


# Product.objects.create(title='New Product 2', description='another one', price='19', summary='sweet')
# Creates a new product using the shell

# Changing fields means needing to update the database
# But what happens to the previous data if you change the model?

