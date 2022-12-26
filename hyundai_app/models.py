from django.db import models

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length = 200)


	def __str__(self):
		return self.name

class MainPageBanner(models.Model):
	headline = models.CharField(max_length = 200)
	sub_headline = models.CharField(max_length = 200, null = True, blank = True)
	images = models.ImageField(null=True, blank=True, upload_to="img")
	created = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return self.headline


class StockCars(models.Model):
	Model_Name = models.CharField(max_length = 200)
	Model_Price = models.CharField(max_length = 200, null = True, blank = True)
	Images = models.ImageField(null=True, blank=True, upload_to="img")
	Fuel = models.CharField(max_length = 20)
	Engine = models.CharField(max_length = 20)
	AWD_RWD = models.CharField(max_length = 20)
	
	created = models.DateTimeField(auto_now_add = True)



	def __str__(self):
		return self.Model_Name





class ModelsCars(models.Model):
	Model_Name = models.CharField(max_length = 200)
	
	Image = models.CharField(max_length = 300)
	Fuel = models.CharField(max_length = 20)
	Engine = models.CharField(max_length = 20)
	AWD_RWD = models.CharField(max_length = 20)
	
	created = models.DateTimeField(auto_now_add = True)



	def __str__(self):
		return self.Model_Name


