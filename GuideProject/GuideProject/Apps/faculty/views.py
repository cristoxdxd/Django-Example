"""
Faculty Views - Django Learning Guide

This module contains views for faculty management.
It demonstrates Django view concepts for faculty operations.
"""

from django.shortcuts import render
from GuideProject.Apps.person.models import Faculty, Student


def faculty(request):
    """
    Faculty overview page.
    
    This demonstrates:
    - Function-based views
    - Aggregation and counting
    - Template rendering with context
    """
    
    # Get all faculties with related student counts
    faculties = Faculty.objects.all().prefetch_related('students')
    
    # Calculate statistics
    total_faculties = faculties.count()
    total_students = Student.objects.filter(is_active=True).count()
    
    # Add student count to each faculty
    faculty_data = []
    for faculty in faculties:
        student_count = faculty.students.filter(is_active=True).count()
        faculty_data.append({
            'faculty': faculty,
            'student_count': student_count
        })
    
    context = {
        'page_title': 'Faculty Management',
        'faculty_data': faculty_data,
        'total_faculties': total_faculties,
        'total_students': total_students,
        'django_concepts': [
            'Model relationships (ForeignKey)',
            'QuerySet optimization (prefetch_related)',
            'Template context data',
            'Aggregation and counting',
            'Function-based views'
        ]
    }
    
    return render(request, 'faculty/faculty.html', context)