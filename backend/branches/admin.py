from django.contrib import admin
from .models import Employee, Branch
from .forms import BranchForm


class EmployeeInline(admin.TabularInline):
    model = Employee
    max_num = 10000


class BranchAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]
    form = BranchForm
    change_form_template = 'change_form.html'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.has_perm('branches.hide_coordinates') and not request.user.is_superuser:
            form.base_fields['latitude'].disabled = True
            form.base_fields['longitude'].disabled = True
            return form
        else:
            form.base_fields['latitude'].disabled = False
            form.base_fields['longitude'].disabled = False
            return form


class EmployeeFilter(admin.ModelAdmin):
    model = Employee
    list_display = ('last_name', 'first_name', 'position', 'branch')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')


admin.site.register(Employee, EmployeeFilter)
admin.site.register(Branch, BranchAdmin)
