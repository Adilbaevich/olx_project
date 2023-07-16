from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

    

class Product1(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField()
    date = models.DateField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Product2(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products2/%Y/%m/%d')
    description = models.TextField()
    date = models.DateField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Product3(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products3/%Y/%m/%d')
    description = models.TextField()
    date = models.DateField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Product4(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products4/%Y/%m/%d')
    description = models.TextField()
    date = models.DateField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


