from django.db import models

# Create your models here.
class Orders(models.Model):
	order_id = models.AutoField(primary_key=True)
	seller = models.ForeignKey('seller.Seller', related_name='seller', blank=False, null=False)
	#couriers = models.ForeignKey('couriers.Courier', related_name='courier', blank=False, null=False)
	docketno = models.ForeignKey('orders.DocketNumbers', related_name = 'docket', blank=False, null=False)
	orderno = models.CharField(max_length=100)
	no_of_packages = models.IntegerField()
	from_pkg_no = models.IntegerField()
	to_pkg_no = models.IntegerField()



class Packages(models.Model):
	package_id = models.AutoField(primary_key=True)
	order = models.ForeignKey('Orders', related_name='order', blank=False, null=False)
	name = models.CharField(max_length=150)
	number = models.IntegerField()
	quantity = models.IntegerField()
	length = models.IntegerField()
	breadth = models.IntegerField()
	height = models.IntegerField()
	weight = models.IntegerField()


class DocketNumbers(models.Model):
	#courier = models.ForeignKey('courier.Courier', related_name='seller', blank=False, null=False)
	docket_number = models.IntegerField(primary_key=True)
	status = models.CharField(max_length=100)
