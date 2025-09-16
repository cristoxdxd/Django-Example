"""
Person Views - Django Learning Guide

This module contains views for student management.
It demonstrates various Django view types and concepts.
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from .models import Student, Faculty


def students(request):
    """
    Function-based view for students overview.
    
    This demonstrates:
    - Function-based views (FBV)
    - Basic template rendering
    - Context data passing
    """
    total_students = Student.objects.count()
    active_students = Student.objects.filter(is_active=True).count()
    faculties = Faculty.objects.all()
    
    context = {
        'page_title': 'Students Overview',
        'total_students': total_students,
        'active_students': active_students,
        'faculties': faculties,
    }
    
    return render(request, 'person/students.html', context)


class ListViewStudents(ListView):
    """
    Class-based view for listing all students.
    
    This demonstrates:
    - Class-based views (CBV)
    - ListView functionality
    - Template naming conventions
    - Pagination (if needed)
    """
    
    model = Student
    template_name = 'person/student_list.html'
    context_object_name = 'students'
    paginate_by = 10  # Show 10 students per page
    
    def get_queryset(self):
        """
        Override the default queryset to add optimizations.
        
        This demonstrates:
        - QuerySet optimization with select_related
        - Filtering active students
        """
        return Student.objects.select_related('faculty').filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        """
        Add extra context data to the template.
        
        This demonstrates:
        - Adding custom context data
        - Using super() to extend parent functionality
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Students'
        context['total_count'] = self.get_queryset().count()
        return context


class ListViewFacultySelect(ListView):
    """
    View for selecting faculty to filter students.
    
    This demonstrates:
    - Custom ListView behavior
    - Template context customization
    """
    
    model = Faculty
    template_name = 'person/faculty_select.html'
    context_object_name = 'faculties'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Select Faculty'
        
        # Add student count for each faculty
        for faculty in context['faculties']:
            faculty.student_count = faculty.students.filter(is_active=True).count()
        
        return context


class ListViewStudentsByFaculty(ListView):
    """
    View for listing students filtered by faculty.
    
    This demonstrates:
    - URL parameter handling
    - Dynamic queryset filtering
    - Error handling with get_object_or_404
    """
    
    model = Student
    template_name = 'person/students_by_faculty.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        """
        Filter students by faculty from URL parameter.
        """
        faculty_name = self.kwargs['faculty']
        self.faculty = get_object_or_404(Faculty, name=faculty_name)
        return Student.objects.filter(
            faculty=self.faculty,
            is_active=True
        ).select_related('faculty')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Students in {self.faculty.name}'
        context['faculty'] = self.faculty
        context['total_count'] = self.get_queryset().count()
        return context