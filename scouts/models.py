from django.db import models

# Create your models here.
class Employee(models.Model):
	photo = models.ImageField(blank=False, upload_to='userprofile')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	id_number = models.CharField(max_length=20, unique=True)
	email = models.EmailField(max_length=100, unique=True)
	adress = models.CharField(max_length=100, unique=True)
	phone_number = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name = "Employee"
		verbose_name_plural = "Employees"

	def __str__(self):
		return self.last_name + ' ' + self.first_name