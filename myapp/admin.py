from django.contrib import admin
from .models import *
import csv

# Register your models here.


# @admin.register(Current_Stock_Field):
# class Current_Stock_Field_Admin(admin.ModelAdmin):
# 	def save_model(self,request,obj,form,change):
# 		csv_file = form.cleaned_data['csv_file']

# 		for row in csv.reader(csv_file):
# 			field1, field2, field3, field4, field5 = row

# 			Current_Stock.objects.update_or_create(
# 					ids = field1,
# 					name = field2,
# 					itemCode = field3,
# 					stock = field4,
# 					amount = field5
# 				)

admin.site.register(Current_Stock)
admin.site.register(Current_Stock_Field)


admin.site.register(Invoice_Profit)
admin.site.register(Invoice_Profit_Field)


admin.site.register(Sales)
admin.site.register(Sales_Field)