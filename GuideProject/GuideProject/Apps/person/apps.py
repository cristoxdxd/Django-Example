"""
Person App Configuration - Django Learning Guide

This file configures the person app.
It demonstrates Django app configuration.
"""

from django.apps import AppConfig


class PersonConfig(AppConfig):
    """
    Configuration for the Person app.
    
    This demonstrates:
    - App configuration
    - Setting default primary key field type
    - App naming conventions
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GuideProject.Apps.person'
    verbose_name = 'Person Management'