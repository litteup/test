from . models import Product



class Product(models.Model):
    product_name = models.CharField(max_length=500)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()


# I. Inserting a new record into the product Model

new_prod = Product('Iphone 14 Pro Max',700000, 1, "The latest Iphone brand, Silver colour, brand new with the Imei 88800998979779")
new_prod.save()
# ii. Get all the records in the Product table
get_all_prod = Product.objects.all() #get all records and store them in the variable
get_all_prod  #This prints all the records stored in the varaiable


# iii. Filter products by their name

filter_prod_by_name = Product.objects.filter(product_name__icontains='Iphone 14')
filter_prod_by_name #prints the filtered product


# iv. Get a single record from the Product table

get_single_product = Product.object.get(pk = 2)
get_single_product_2 = Product.object.get(id = 2)

# v. Change a product price

#using the new_prod variable used in add a record to the database earlier above
new_prod.product_price =1000000
new_prod.save()
