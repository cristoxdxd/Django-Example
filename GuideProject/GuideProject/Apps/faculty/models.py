"""
Faculty Models - Django Learning Guide

This module contains models for faculty management.
Since Faculty is already defined in person.models, we import it here.
"""

# Import the Faculty model from person app to avoid duplication
from GuideProject.Apps.person.models import Faculty, Student

# This file exists to maintain the app structure, but the actual
# models are defined in the person app to avoid circular imports.