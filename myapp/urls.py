from django.urls import path
# from myapp.views import *
from .import views



urlpatterns = [
	path('',views.main_views,name="main_views"),
	# path('stock/upload/',views.field_Current_Stock,name="Current_Stock_Field"),
	# path('sales/upload/',views.field_Sales,name="field_Sales"),
	# path('invoice/upload/',views.field_Invoice_Profit,name="field_Invoice_Profit"),
	path('stock/',views.view_Current_Stock,name="Current_Stock_View"),
	path('invoice/',views.view_Invoice,name="view_Invoice"),
	path('sales/',views.view_Sales,name="view_Sales"),
]


