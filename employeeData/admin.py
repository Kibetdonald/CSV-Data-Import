from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee


class EmployeeDetail(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'years_of_experience', 'salary' )
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'years_of_experience', 'salary']
    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


admin.site.register(Employee, EmployeeDetail)
