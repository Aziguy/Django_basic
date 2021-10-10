from django.contrib import admin
from . models import Employee
from django.utils.html import format_html

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):

	def thumbnail(self, object):
		return format_html('<img src="{}" style="height: 40px; width: 40px; border-radius:50%;">'.format(object.photo.url))

	thumbnail.short_description = 'Employee Photo'

	list_display = ('thumbnail','email', 'first_name', 'last_name', 'phone_number')
	list_display_links = ('thumbnail','email', 'first_name', 'last_name')
	readonly_fields = ()
	ordering = ('-first_name',)
	search_fields = ('id_number', 'first_name', 'last_name')
	list_editable = ()
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Employee, EmployeeAdmin)