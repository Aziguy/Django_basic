from django.shortcuts import render
from . models import Employee

# Create your views here.
def scouts(request):
	employee = Employee.objects.all()
	data = {
		'employee':employee,
	}
	return render(request, 'employee-lists.html', data)