from django.db import models

# Create your models here.
class People(models.Model):
    identity_number = models.CharField(max_length=10000,unique=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    other_names= models.CharField(max_length=100)

    def __str__(self):
        return ('Name: {} {}'.format(self.first_name,self.surname))

class Address(models.Model):
    people = models.ForeignKey(People,on_delete=models.CASCADE)
    home_address = models.CharField(max_length=500)
    work_address = models.CharField(max_length=500)
    postal_address = models.CharField(max_length=500)
    #ManyToOneRel(People)

    def __str__(self):
        return f'Home address: {self.home_address}.'
class Doctor(models.Model):

    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=500)
    people = models.ManyToManyField(People)

    def __str__(self):
        return f'Dr {self.f_name} {self.l_name}.'


class Product(models.Model):
    product_name = models.CharField(max_length=500)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()

    def __str__(self):
        return f'Product name: {self.product_name}, Price: {self.product_price}.'

class Bio(models.Model):
    SEX = {
        ('m', 'Male'),
        ('f', 'Female'),
    }

    people = models.ForeignKey(People,on_delete=models.CASCADE)
    email = models.EmailField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    bio_sex = models.CharField(max_length=1,choices=SEX)
    people = models.OneToOneField(People,on_delete=models.CASCADE)


    def __str__(self):
        return f'Sex: {self.bio_sex}, Date of birth: {self.date_of_birth}.'
