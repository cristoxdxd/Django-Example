"""
Person Admin Configuration - Django Learning Guide

This module configures the Django admin interface for Person models.
It demonstrates admin customization and management interface best practices.
"""

from django.contrib import admin
from .models import Student, Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    """
    Admin configuration for Faculty model.
    
    This demonstrates:
    - Admin registration using decorator
    - Customizing list display
    - Adding filters and search
    - Organizing fields in forms
    """
    
    list_display = ('name', 'dean', 'established_date', 'student_count')
    list_filter = ('established_date',)
    search_fields = ('name', 'dean', 'description')
    ordering = ('name',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Administration', {
            'fields': ('dean', 'established_date'),
            'classes': ('collapse',)
        }),
    )
    
    def student_count(self, obj):
        """Display the number of active students in this faculty."""
        return obj.students.filter(is_active=True).count()
    
    student_count.short_description = 'Active Students'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Student model.
    
    This demonstrates:
    - Complex admin customization
    - List filters and search
    - Readonly fields
    - Custom methods in admin
    """
    
    list_display = (
        'get_full_name', 'student_id', 'email', 'faculty', 
        'enrollment_date', 'is_active'
    )
    list_filter = (
        'faculty', 'is_active', 'enrollment_date', 'graduation_year'
    )
    search_fields = (
        'first_name', 'last_name', 'email', 'student_id'
    )
    list_editable = ('is_active',)
    ordering = ('last_name', 'first_name')
    
    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'last_name'),
                'email',
                'date_of_birth',
                'phone_number',
                'address'
            )
        }),
        ('Academic Information', {
            'fields': (
                'student_id',
                'faculty',
                'enrollment_date',
                'graduation_year',
                'is_active'
            )
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def get_full_name(self, obj):
        """Display the student's full name in the admin list."""
        return obj.get_full_name()
    
    get_full_name.short_description = 'Full Name'
    get_full_name.admin_order_field = 'last_name'
    
    # Add some bulk actions
    actions = ['mark_inactive', 'mark_active']
    
    def mark_inactive(self, request, queryset):
        """Bulk action to mark students as inactive."""
        updated = queryset.update(is_active=False)
        self.message_user(
            request, 
            f'{updated} students were successfully marked as inactive.'
        )
    mark_inactive.short_description = 'Mark selected students as inactive'
    
    def mark_active(self, request, queryset):
        """Bulk action to mark students as active."""
        updated = queryset.update(is_active=True)
        self.message_user(
            request, 
            f'{updated} students were successfully marked as active.'
        )
    mark_active.short_description = 'Mark selected students as active'