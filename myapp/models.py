from django.db import models
from django.utils import timezone
# from decimal import Decimal


# Create your models here.




class Current_Stock(models.Model):
	ids = models.CharField(max_length=1000,null=False,blank=False)
	name = models.CharField(max_length=100,null=False,blank=False)
	itemCode = models.CharField(max_length=100,null=True,blank=True)
	stock = models.CharField(max_length=5,null=False,blank=False)
	price = models.IntegerField(null=False,blank=False)
	amount = models.CharField(max_length=5,null=False,blank=False)
	uploaded_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name




class Current_Stock_Field(models.Model):
	file = models.FileField(upload_to='uploads/')
	uploaded_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return str(self.uploaded_date)





class Invoice_Profit(models.Model):
	ids = models.CharField(max_length=1000,null=False,blank=False)
	date = models.CharField(max_length=100,null=False,blank=False)
	invoice_numb = models.CharField(max_length=100,null=False,blank=False)
	customer_name = models.CharField(max_length=100,null=False,blank=False)
	phone_numb = models.CharField(max_length=100,null=False,blank=False)
	amount = models.CharField(max_length=100,null=False,blank=False)
	cogs = models.CharField(max_length=100,null=False,blank=False)
	margin = models.CharField(max_length=100,null=False,blank=False)
	uploaded_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.customer_name



class Invoice_Profit_Field(models.Model):
	file = models.FileField(upload_to='invoice/')
	uploaded_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.uploaded_date}"






class Sales(models.Model):
	ids = models.CharField(max_length=1000,null=False,blank=False)
	itemName = models.CharField(max_length=100,null=False,blank=False)
	quantity = models.CharField(max_length=100,null=False,blank=False)
	amount = models.CharField(max_length=100,null=False,blank=False)
	tax = models.CharField(max_length=100,null=True,blank=True)
	tax_amount = models.CharField(max_length=100,null=False,blank=False)
	total_amount = models.CharField(max_length=100,null=False,blank=False)
	uploaded_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.itemName



class Sales_Field(models.Model):
	file = models.FileField(upload_to='sales/')
	uploaded_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return f"{self.uploaded_date}"



