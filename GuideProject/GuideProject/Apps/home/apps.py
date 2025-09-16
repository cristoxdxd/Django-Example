"""
Home App Configuration - Django Learning Guide

This file configures the home app.
It demonstrates Django app configuration.
"""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration for the Home app.
    
    This demonstrates:
    - App configuration
    - Setting default primary key field type
    - App naming conventions
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GuideProject.Apps.home'
    verbose_name = 'Home'