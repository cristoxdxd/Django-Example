"""
Faculty App Configuration - Django Learning Guide

This file configures the faculty app.
It demonstrates Django app configuration.
"""

from django.apps import AppConfig


class FacultyConfig(AppConfig):
    """
    Configuration for the Faculty app.
    
    This demonstrates:
    - App configuration
    - Setting default primary key field type
    - App naming conventions
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GuideProject.Apps.faculty'
    verbose_name = 'Faculty Management'