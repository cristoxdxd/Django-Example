"""
Home Views - Django Learning Guide

This module contains views for the home page of the University management system.
It demonstrates basic Django view concepts for beginners.
"""

from django.shortcuts import render


def index(request):
    """
    Home page view.
    
    This is a function-based view (FBV) - the simplest type of view in Django.
    It takes an HTTP request and returns an HTTP response.
    
    Args:
        request: HttpRequest object containing metadata about the request
        
    Returns:
        HttpResponse: Rendered template with context data
    """
    # Context data to pass to the template
    context = {
        'page_title': 'University Management System',
        'welcome_message': 'Welcome to our Django Learning Guide!',
        'features': [
            'Student Management',
            'Faculty Management', 
            'Course Management',
            'Modern Bootstrap UI',
            'Complete CRUD Operations'
        ],
        'django_concepts': [
            'Models (Database layer)',
            'Views (Business logic)',
            'Templates (Presentation layer)',
            'URL routing',
            'Admin interface',
            'Forms and validation'
        ]
    }
    
    return render(request, 'home/index.html', context)